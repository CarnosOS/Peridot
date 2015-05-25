from KPython.Lib.archersys.Dronesseus.contrib.Point import Point
class Rectangle:
    """Rectangle class using Point, width and height"""

    def __init__(self, initP, initW, initH):

        self.location = initP
        self.width = initW
        self.height = initH
    
    def getHeight(self):
        return self.height
    def getWidth(self):
        return self.width
    def __str__(self):
        return str(self.getHeight()) + " by " + str(self.getWidth())
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width * 2) + (self.height * 2)
    
    def transpose(self):
        temp = self.width
        self.width = self.height
        self.height = temp
   
    def contains(self,item):
        return self.location == item  
    def diagonal(self):
        d = (self.width**2 + self.height**2) ** 0.5
        return d
    def __eq__(self, other):
        return self.location == other.location
