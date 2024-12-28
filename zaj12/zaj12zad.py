import math


def checkPoint(f):
    def check(p1, p2):
        if p2[0] < 0 or p2[0] > 100 or p2[1] < 0 or p2[1] > 100:
            raise ValueError("Nie mozesz dodac/odjac takiej liczby!")
        f(p1, p2)

    return check


class Point(object):
    def __init__(self):
        self.x = 0
        self.y = 0

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, val):
        self._x = val

    @y.setter
    def y(self, val):
        self._y = val

    @checkPoint
    def plus(self, p):
        self.x += p[0]
        self.y += p[1]

    @checkPoint
    def minus(self, p):
        self.x -= p[0]
        self.y -= p[1]

    def wypisz(self):
        print(f"X={self.x} Y={self.y}")


p1 = Point()
p1.plus((5, 1))
p1.wypisz()
# p1.plus((101, 1))
# p1.wypisz()

p2 = Point()
p2.plus((1, 1))

p3 = Point()
p3.plus((1, 0))

p4 = Point()
p4.plus((5, 0))


def checkPointsCount(f):
    def check(*points):
        if len(points) < 3 or len(points) > 4:
            raise ValueError("Musi byc albo 3 albo 4 punktow")
        return f(*points)

    return check


def wypiszPunkty(f):
    def wypiszP(*points):
        print("PUNKTY")
        for point in points:
            point.wypisz()
        return f(*points)

    return wypiszP


class Figury(object):

    @staticmethod
    @checkPointsCount
    def obwod(*points):
        ob = 0
        for i in range(1, len(points) + 1):
            ob += math.sqrt(
                (points[i - 1].x - points[i % len(points)].x) ** 2 + (points[i - 1].y - points[i % len(points)].y) ** 2)
        return ob

    @staticmethod
    @checkPointsCount
    @wypiszPunkty
    def pole(*points):
        p = Figury.obwod(*points) / 2

        dl_bokow = []
        for i in range(1, len(points) + 1):
            dl_bokow.append(math.sqrt((points[i - 1].x - points[i % len(points)].x) ** 2 + (
                    points[i - 1].y - points[i % len(points)].y) ** 2))

        if len(points) == 3:
            return math.sqrt(p * (p - dl_bokow[0]) * (p - dl_bokow[1]) * (p - dl_bokow[2]))
        else:
            return math.sqrt((p - dl_bokow[0]) * (p - dl_bokow[1]) * (p - dl_bokow[2]) * (p - dl_bokow[3]))


p = Figury.pole(p1, p2, p3)
print("Pole", p)

p = Figury.pole(p1, p2, p3, p4)
print("Pole", p)


class Zliczanie(object):
    counter = {}

    def __init__(self, f):
        self._p = f
        Zliczanie.counter[self._p.__name__] = 0

    def __call__(self):
        Zliczanie.counter[self._p.__name__] += 1
        self._p()


@Zliczanie
def test1():
    print("TEST1")


@Zliczanie
def test2():
    print("TEST2")


test1()
test2()
test2()

print(Zliczanie.counter)
