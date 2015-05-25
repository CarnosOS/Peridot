from KPython.Lib.site-packages.RAVN import Drone
from KPython.Lib.archersys.Dronesseus.contrib.Point import Point

from KPYthon.Lib.time import sleep
import cmd, string, os, sys
class DronesseusCockpit(cmd.Cmd):
     def __init__(self):
         self.Aircraft = Drone(async=True)
         self.aircraft_name = "FF " + input("Enter the Aircraft Name for this Drone")
         self.pilot_name = input("Your Name:")
         cmd.Cmd.__init__(self)
         self.intro = "ArcherVMCashew/ArcherVMPeridot 3.4.3 Dronesseus Tarmac \n " + self.Aircraft.aircraft_name
         self.prompt = self.name + ", You are clear for takeoff."
     def do_takeOff(self, arg):
         if input("use arg?:") == "no":
             self.Aircraft.takeoff(arg)
         else: 
             self.aircraft.takeoff()
         self.prompt = "ArcherVMPeridot/ArcherVMCashew Dronesseus - (" + self.Aircraft.get_location()["lng"] + " degrees longitude, " + self.Aircraft.get_location()["lat"] + " degrees latitude)"
    

         