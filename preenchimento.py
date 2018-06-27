from bresenham import *
from ponto import *


def drawPolygon(coordinates):
    coord = []
    info = []
    for i in range(0,len(coordinates)+1):
        if i == (len(coordinates)):
            break
        p = coordinates[i-1]
        np = coordinates[i]
        coord.extend(Bresenham(Point(p[0], p[1]), Point(np[0], np[1])))
    return coord




fill = []
def FloodFill(point, edge):
    global fill
    current = point
    if not(current in edge) and not(current in fill):
        fill.append(current)
        FloodFill(Point(point.x + 1, point.y), edge)
        FloodFill(Point(point.x, point.y+1), edge)
        FloodFill(Point(point.x-1, point.y), edge)
        FloodFill(Point(point.x, point.y-1), edge)

