import Point


class Vector:
    def __init__(self, p1=Point.Point(0,0), p2=Point.Point(0,0)):
        self.x = p2.x - p1.x
        self.y = p2.y - p1.y
        
    def cross(self, vt):
        return (self.x*vt.y) - (self.y*vt.x)
