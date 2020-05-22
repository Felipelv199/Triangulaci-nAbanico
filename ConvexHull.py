import Point as pt
import Vector as vt


def counterclockwise(a, b, c):
    v1 = vt.Vector(a, b)
    v2 = vt.Vector(b, c)
    orientation = v1.cross(v2)
    if orientation >= 0:
        return True
    else:
        return False


def sort_by_angle(arr, pivot):
    aux_arr = []
    for point in arr:
        point.setAngle(pivot)
        aux_arr.append(point)
    aux_arr.sort(key=get_angle, reverse=True)
    return aux_arr


def get_angle(p):
    return p.angle


class ConvexHull:

    def __init__(self, points):
        self.points = points
        self.lowest_point = pt.Point(0, 0)
        self.R = []

    def set_lowest_point(self):
        arr = self.points
        lp = arr[0]
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                if i != j:
                    if lp.y > arr[j].y:
                        lp = arr[j]
                    elif lp.y > arr[i].y:
                        lp = arr[i]
                    elif lp == arr[i].y and lp == arr[j].y:
                        if lp.x > arr[i].x:
                            lp = arr[i]
                        elif lp.x > arr[j].x:
                            lp = arr[j]
        arr.remove(lp)
        self.lowest_point = lp

    def algorithm(self):
        self.set_lowest_point()
        lp = self.lowest_point
        arr = sort_by_angle(self.points, lp)
        convex_hull = [lp, arr.pop(), arr.pop()]
        c = arr.pop()

        while True:
            b = convex_hull[-1]
            a = convex_hull[-2]
            if counterclockwise(a, b, c):
                convex_hull.append(c)
                if len(arr) > 0:
                    c = arr.pop()
                else:
                    break
            else:
                convex_hull.pop()
        self.points.append(lp)
        self.R = convex_hull

