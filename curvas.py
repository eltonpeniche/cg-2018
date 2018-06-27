import matplotlib.pyplot as plt


class l(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __call__(self, t):
        ret = list(self.p1)
        for i in range(len(ret)):
            ret[i] = (1 - t) * self.p1[i] + t * self.p2[i]
        print(ret)
        return tuple(ret)


#linha1 = l((0, 0), (10, 10))


class f(object):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def __call__(self, t):
        ret = list(self.p1)
        for i in range(len(ret)):
            ret[i] = (1 - t ** 2) * self.p1[i] + 2 * t * (1 - t) * self.p2[i] + t ** 2 * self.p3[i]
        return tuple(ret)


#curve1 = f((0, 0), (10, 20),(20,10))

class g(object):
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def __call__(self, t):
        ret = list(self.p1)
        for i in range(len(ret)):
            ret[i] = (1 - t) ** 3 * self.p1[i] + 3 * t * (1 - t) ** 2 * self.p2[i] + 3 * t ** 2 * (1 - t) * self.p3[
                i] + t ** 3 * self.p4[i]
        return tuple(ret)

