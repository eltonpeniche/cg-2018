import matplotlib.pyplot as plt
from ponto import *

def Bresenham(p1, p2):
    x = p1.x
    y = p1.y

    dx = p2.x - p1.x
    dy = p2.y - p1.y
    inclination = 0

    if dx < 0:  # caso ponto final < ponto inicial
        return Bresenham(p2, p1)


    list = []
    list.append(p1)
    if dy < 0:
        inclination = -1
    else:
        inclination = 1

    if (dx >= inclination * dy): # m<=1
        if dy < 0:  # caso y2<y1
            d = 2 * dy + dx
            while (x < p2.x):
                if (d < 0):  # escolhido é o I
                    d += 2 * (dy + dx)
                    x += 1
                    y -= 1
                else:  # escolhido é o S
                    d += 2 * dy
                    x += 1  # varia apenas no eixo x
                list.append(Point(x, y))

        else:  # caso y1<y2
            d = 2 * dy - dx
            while (x < p2.x):
                if (d < 0):  # escolhido é o I
                    d += 2 * dy
                    x += 1  # varia apenas no eixo x
                else:  # escolhido é o S
                    d += 2 * (dy - dx)
                    x += 1
                    y += 1
                list.append(Point(x, y))

    else:  # |m|>1
        if (dy < 0):  # // caso y2<y1
            d = dy + 2 * dx
            while (y > p2.y):
                if (d < 0):
                        d += 2 * dx
                        y -= 1  # varia apenas no eixo y
                else:
                    d += 2 * (dy + dx)
                    x += 1
                    y -= 1
                list.append(Point(x, y))

        else:  # caso y1<y2
            d = dy - 2 * dx
            while (y < p2.y):
                if (d < 0):
                    d += 2 * (dy - dx)
                    x += 1
                    y += 1
                else:
                    d += -2 * dx
                    y += 1  # varia apenas no eixo y
                list.append(Point(x, y))

    # lista.append([x,y])
    return list


def drawLine(p1, p2):
    list = Bresenham(p1, p2)
    for i in range(0, len(list)):
        plt.plot([list[i].x], [list[i].y], 'rs')
    plt.axis([0, len(list), 0, len(list)])
    #plt.axis([0, 60, 0, 60]) #para o recorte
    plt.grid(1)
    plt.show()