import Point as pt
import random as r
import ConvexHull


def generate_random_points(n):
    arr = []
    for _ in range(n):
        point = pt.Point(r.randrange(100, 900), r.randrange(100, 620))
        arr.append(point)
    return arr


points = generate_random_points(100)
CH = ConvexHull.ConvexHull(points)
CH.algorithm()
convex_hull = CH.R


