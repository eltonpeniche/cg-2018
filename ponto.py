

class Point:
    def __init__(self, x, y, bs = 'bs'):
        self.x = x
        self.y = y
        self.cor = 'bs'

    def __str__(self):
        return "[%d,%d]" % (self.x, self.y)

    def __eq__(self, p2):
        if self.x == p2.get_x() and self.y == p2.get_y():
            return True
        return False

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def set_x(self, x):
        self.y = x

    def cof_angular(self, p):
        deltax = p.get_x() - self.get_x()
        deltay = p.get_y() - self.get_y()

        if deltax == 0:
            return 0
        return deltay / deltax


def show(l):
    for i in range(len(l)):
        print(l[i])
