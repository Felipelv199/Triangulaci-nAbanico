import pygame as pg
import Point as Pt
import random as r
import Segment as Sg
import ConvexHull


def generate_random_points(n):
    arr = []
    for _ in range(n):
        point = Pt.Point(r.randrange(50, 950), r.randrange(50, 670))
        arr.append(point)
    return arr


points = generate_random_points(100)
CH = ConvexHull.ConvexHull(points)
CH.algorithm()
convex_hull = CH.R

leftest_vertex = None
for vertex in convex_hull:
    if leftest_vertex is not None:
        if vertex.x < leftest_vertex.x:
            leftest_vertex = vertex
        elif vertex.x == leftest_vertex.x:
            if vertex.y < leftest_vertex.y:
                leftest_vertex = vertex
    else:
        leftest_vertex = vertex

triangulation_segments = []
for vertex in convex_hull:
    if vertex is not leftest_vertex:
        triangulation_segments.append(Sg.Segment(leftest_vertex, vertex))


pg.init()
screen = pg.display.set_mode((1000, 720))
pg.display.set_caption('Graphics')
animationTimer = pg.time.Clock()
endProgram = False

while not endProgram:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            endProgram = True

    screen.fill((255, 255, 255))

    for point in points:
        x = int(point.x)
        y = int(point.y)
        pg.draw.circle(screen, (0, 0, 255), (x, y), 2)

    for i in range(len(convex_hull)):
        if i < len(convex_hull) - 1:
            p1 = convex_hull[i]
            x1 = int(p1.x)
            y1 = int(p1.y)

            p2 = convex_hull[i + 1]
            x2 = int(p2.x)
            y2 = int(p2.y)
            pg.draw.line(screen, (0, 255, 0), (x1, y1), (x2, y2), 1)
        else:
            p1 = convex_hull[i]
            x1 = int(p1.x)
            y1 = int(p1.y)

            p2 = convex_hull[0]
            x2 = int(p2.x)
            y2 = int(p2.y)
            pg.draw.line(screen, (0, 255, 0), (x1, y1), (x2, y2), 1)

    x = leftest_vertex.x
    y = leftest_vertex.y
    for segment in triangulation_segments:
        p1 = segment.point1
        x1 = int(p1.x)
        y1 = int(p1.y)

        p2 = segment.point2
        x2 = int(p2.x)
        y2 = int(p2.y)
        pg.draw.line(screen, (0, 0, 0), (x1, y1), (x2, y2), 1)

    animationTimer.tick(100)
    pg.display.update()
