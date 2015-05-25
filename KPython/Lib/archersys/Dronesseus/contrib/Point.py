from KPython.Lib.site-packages.RAVN import Drone
import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    def __gt__(a,b):
        return a.getX() > b.getX() and a.getY() > b.getY()
    def __sub__(a, b):
        if a > b:
            return (a.getX() - b.getX(),a.getY() - b.getY())
        elif b > a:
            return (b.getX() - a.getX(),b.getY() - q.getY())
    def get_line_to(self, point):
        return point - self
    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    def reflect_x(self):
        return str(self.getX())+ "," +str(-self.getY()) 
    def distanceFromPoint(self, otherP):
        dx = (otherP.getX() - self.x)
        dy = (otherP.getY() - self.y)
        return math.sqrt(dy**2 + dx**2)
    def slope_from_origin(self):
        if self.x == 0:
            return None
        else:
             return self.y / self.x
    def radius_and_center(self,point2,center):
        radius = self.get_line_to(center)
        return (radius[0],radius[1])
        
     
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def __str__(self):
        return str(self.x) + "," + str(self.y)
