import Point as Pt


class Segment:
    
    def __init__(self, point1=Pt.Point(0,0), point2=Pt.Point(0,0)):
        self.name = ""
        self.point1 = point1
        self.point2 = point2

    def __repr__(self):
        return f"[{self.point1},{self.point2}]"

    def __str__(self):
        return "[" + str(self.point1) + "," + str(self.point2) + "]"

    def calculate_intersection(self, segment_2):
        x1s1 = self.point1.x
        x2s1 = self.point2.x
        y1s1 = self.point1.y
        y2s1 = self.point2.y
        
        x1s2 = segment_2.point1.x
        x2s2 = segment_2.point2.x
        y1s2 = segment_2.point1.y
        y2s2 = segment_2.point2.y
        
        if x2s1 - x1s1 == 0:
            m1 = 99999999
        else:
            m1 = (y2s1 - y1s1) / (x2s1 - x1s1)
        
        if x2s2 - x1s2 == 0:
            m2 = 99999999
        else:
            m2 = (y2s2 - y1s2) / (x2s2 - x1s2)

        den = m2 - m1
        
        x = ((m2 * x1s2 - y1s2) - (m1 * x1s1 - y1s1)) / den
        y = ((m1 * (m2 * x1s2 - y1s2)) - (m2 * (m1 * x1s1 - y1s1))) / den
        
        return Pt.Point(x, y)
