"""
RAVN Smart Drone Platform
Copyright (C) 2014 RaptorBird Robotics Inc.
<http://www.raptorbird.com/>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; Version 2

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

from ws4py.client.threadedclient import WebSocketClient
import time

class RavnClient(WebSocketClient):
    """
    Ravn WebSocket Client that connects to Ravn Server
    """
    def __init__(self, url, protocols=None, extensions=None,\
        heartbeat_freq=.2, ssl_options=None, headers=None):
        """
        Initializes the data structure for drone status
        """
        WebSocketClient.__init__(self, url, protocols, \
            extensions, heartbeat_freq, ssl_options, headers)
        self.ravn = {
            "mode": "",
            "location": {
                "lat": 0.0,
                "lng": 0.0,
                "alt": 0,
            },
            "attitude": {
                "roll": 0.0,
                "pitch": 0.0,
                "yaw": 0.0
            },
            "velocity": {
                "x": 0.0,
                "y": 0.0,
                "z": 0.0
            },
            "armed": False,
            "airspeed": 0.0,
            "groundspeed": 0.0,
        }
        self.wp_reached = False
        self.takeoff = False
        self.land = True
        self.buffer = []

    def closed(self, code, reason=None):
        print "Closed down", code, reason

    def received_message(self, m):
        """
        Parses Data recieved and stores it in the appropriate location
        """
        m = str(m)
        if m[0] == "%":
            data = m.split(',')
            data.pop(0) # remove % from message
            self.ravn["mode"] = data[0]
            self.ravn["location"]["lat"] = float(data[1])
            self.ravn["location"]["lng"] = float(data[2])
            self.ravn["location"]["alt"] = float(data[3])
            self.ravn["attitude"]["roll"] = float(data[4])
            self.ravn["attitude"]["pitch"] = float(data[5])
            self.ravn["attitude"]["yaw"] = float(data[6])
            self.ravn["velocity"]["x"] = float(data[7])
            self.ravn["velocity"]["y"] = float(data[8])
            self.ravn["velocity"]["z"] = float(data[9])
            self.ravn["armed"] = bool(data[10])
            # Only when airspeed sensor connected
            self.ravn["airspeed"] = float(data[11])
            self.ravn["groundspeed"] = float(data[12])
        elif m[0] == "@":
            self.wp_reached = True
        elif m[0] == "T":
            self.takeoff = True
            self.land = False
        elif m[0] == "L":
            self.takeoff = False
            self.land = True


class Drone(object):
    """
    API object used to control the Ravn Drone
    """
    def __init__(self, host='localhost', port=9000, async=False):
        """
        Connects to Ravn Server.

        Keyword Arguments:
        host -- the address of the Ravn Server (default localhost)
        port -- the port of the Ravn Server (default 9000)
        """
        address = 'ws://' + host + ':' + str(port)
        self.async = async
        self.ravn_client = RavnClient(address, protocols=['http-only', 'chat'])
        self.ravn_client.connect()

    def takeoff(self, alt=2, debug=True, async=False):
        """
        Takes off at current position,
        and hovers at a height specified in meters

        Keyword Arguments:
        alt -- the altitude to takeoff in meters (default 2)
        async -- True = Non Blocking Call, False = Blocking Call (default False)

        Return:
        True:   If command was confirmed by the server
        False:  If command was not confirmed by the server
        """
        if debug:
            time.sleep(15)
        self.ravn_client.send("T,"+str(alt))
        if async or self.async:
            return
        while not self.ravn_client.takeoff: # Check if its in air yet
            time.sleep(.1)

    def land(self, async=False):
        """
        Lands the drone at current latitude/longtitude

        Keyword Arguments:
        async -- True = Non Blocking Call, False = Blocking Call (default False)

        Return
        True:   If command was confirmed by the server
        False:  If command was not confirmed by the server
        """
        self.ravn_client.send("L")
        if async or self.async:
            return
        while not self.ravn_client.land:  # Check if its on ground
            time.sleep(.1)

    def goto(self, latitude=360, longtitude=360, altitude=150, async=False):
        """
        Go to a Location

        Keyword Arguments:
        altitude -- Altitude, (default Current Altitude)
        latitude -- Latitude, (default Current Latitude)
        longtitude -- Longtitude, (default Current Longtitude)
        async -- True = Non Blocking Call, False = Blocking Call (default False)

        Return:
        True:   If command was confirmed
        False:  If command was not confirmed
        """
        msg = ','.join(["G", str(latitude), str(longtitude), str(altitude)])
        self.ravn_client.wp_reached = False
        self.ravn_client.send(msg)
        if async or self.async:
            return
        while not self.ravn_client.wp_reached:  # Check if it reached waypoint
            time.sleep(.1)

    def gotoalt(self, alt=150, async=False):
        """
        Go to Altitude in meters

        Keyword Arguments:
        async -- True = Non Blocking Call, False = Blocking Call (default False)

        Return:
        True:   If command was confirmed
        False:  If command was not confirmed
        """
        msg = ''.join(["G", "360", "360", str(alt)])
        self.ravn_client.wp_reached = False
        self.ravn_client.send(msg)
        if async or self.async:
            return
        while not self.ravn_client.wp_reached:  # Check if it reached waypoint
            time.sleep(.1)

    def is_armed(self):
        """
        Get the status of the drone

        Return:
        True:   If drone is armed
        False:  If drone is not armed
        """
        return self.ravn_client.ravn["armed"]

    def get_location(self):
        """
        Get Current Location

        Return:
        An array:
        {
            "lat": Current latitude,
            "lng": Current longtitude,
            "alt": Current Altitude
        }
        """
        return self.ravn_client.ravn["location"]

    def get_velocity(self):
        """
        Get the Velocity of the drone

        Return:
        An array:
        {
            "x": Horizontal Transalational Velocity - Side-to-Side,
            "y": Horizontal Transalational Velocity - Front-to-Back,
            "z": Vertical Velocity - Up-to-Down
        }
        """
        return self.ravn_client.ravn["velocity"]

    def get_altitude(self):
        """
        Get the Altitude of the drone in meters

        Return:
        float:  Altitude in meters
        """
        return self.ravn_client.ravn["attitude"]

    def get_airspeed(self):
        """
        Get the airspeed of drone if a airspeed sensor is attatched

        Return:
        float: airspeed in m/s
        """
        return self.ravn_client.ravn["airspeed"]

    def get_groundspeed(self):
        """
        Get the speed of the drone relative to the ground

        Return:
        float: groundspeed in m/s
        """
        return self.ravn_client.ravn["groundspeed"]

    def get_mode(self):
        """
        Get the status of the drone

        Return:
        string: mode of the APM
        "STABILIZE" - manual control mode
        "LOITER" - GPS based manual control mode
        "GUIDED" - GPS based navigation (Goto a Location)
        "LAND"   - Landing mode, slowly touches down at current location
        """
        return self.ravn_client.ravn["mode"]

    def close(self):
        """
        Closes the connection, and releases the thread
        """
        self.ravn_client.close()
