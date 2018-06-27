import matplotlib.pyplot as plt

from ponto import *


def octants(p):
    list = [Point(p.y, p.x)]  # octante 2
    list.append(Point(p.y, -p.x))  # octante 3
    list.append(Point(-p.x, p.y))  # octante 4
    list.append(Point(-p.x, -p.y)) # octante 5
    list.append(Point(-p.y, -p.x)) # octante 6
    list.append(Point(-p.y, p.x))  # octante 7
    list.append(Point(p.x, -p.y))  # octante 8
    return list


def CircleMidPoint(radius):
    y = radius
    x = 0
    list = [Point(x, y)]
    list.extend(octants(Point(x, y)))
    p = 1 - radius

    while (x < y):
        x += 1
        if (p < 0):
            # p += (2*x)+1
            p += (2 * x) + 3
        else:
            y -= 1
            # p += (2*x)+1-(2*y)
            p += (2 * x) - (2 * y) + 5
        list.extend(octants(Point(x, y)))
        if not (Point(x, y) in list):
            list.append(Point(x, y))

    return list


def drawcircle(r):
    list = CircleMidPoint(r)
    for i in range(0, len(list)):
        plt.plot([list[i].x], [list[i].y], 'ro')

    plt.axis([-(r+10), r+10, -(r+10), r+10])
    plt.grid(1)
    plt.show()
