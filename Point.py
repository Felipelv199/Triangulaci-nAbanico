import math as m


class Point:

    def __init__(self, x, y):
        self.name = ""
        self.x = x
        self.y = y
        self.segment = None
        self.angle = 0

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def setAngle(self, p0):
        co = self.y - p0.y
        ca = self.x - p0.x
        self.angle = m.degrees(m.atan2(co, ca))