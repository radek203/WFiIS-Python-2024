import math
import random

import matplotlib.pyplot as plt


class IFS:
    def __init__(self, wsp, prawd=()):
        """
        Metoda inicjalizacyjna

        :param wsp: Zestaw wspolczynnikow
        :param prawd: Prawdopodobienstwa na dany zestaw
        :return: bezposrednio nie zwracamy nic
        """
        self.wsp = wsp
        self.points = []
        self.points.append((0, 0))
        self.prawd = prawd if len(prawd) > 0 else [1 for _ in wsp]

    def przeksztalcenie(self, iternum):
        """
        Funkcja oblicza kolejne punkty do narysowania

        :param iternum: Ilosc punktow
        :return: bezposrednio nie zwracamy nic
        """
        for i in range(1, iternum):
            wylosowane = random.choices(self.wsp, weights=self.prawd, k=1)[0]
            x = wylosowane[0] * self.points[i - 1][0] + wylosowane[1] * self.points[i - 1][1] + wylosowane[2]
            y = wylosowane[3] * self.points[i - 1][0] + wylosowane[4] * self.points[i - 1][1] + wylosowane[5]
            self.points.append((x, y))

    def rysuj(self):
        """
        Funkcja rysuje wykres na podstawie obliczonych punktow

        :return: bezposrednio nie zwracamy nic
        """
        x_values, y_values = zip(*self.points)
        plt.scatter(x_values, y_values, s=2)

        plt.title('Wykres')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()


ifs1 = IFS(((0.787879, -0.424242, 1.758647, 0.242424, 0.859848, 1.408065), (-0.121212, 0.257576, -6.721654, 0.151515, 0.05303, 1.377236), (0.181818, -0.136364, 6.086107, 0.090909, 0.181818, 1.568035)), (0.90, 0.05, 0.05))
ifs1.przeksztalcenie(10000)
ifs1.rysuj()

ifs2 = IFS(((0, 0.053, -7.083, -0.429, 0, 5.43), (0.143, 0, -5.619, 0, -0.053, 8.513), (0.143, 0, -5.619, 0, 0.083, 2.057), (0, 0.053, -3.952, 0.429, 0, 5.43), (0.119, 0, -2.555, 0, 0.053, 4.536), (-0.0123806, -0.0649723, -1.226, 0.423819, 0.00189797, 5.235),
            (0.0852291, 0.0506328, -0.421, 0.420449, 0.0156626, 4.569), (0.104432, 0.00529117, 0.976, 0.0570516, 0.0527352, 8.113), (-0.00814186, -0.0417935, 1.934, 0.423922, 0.00415972, 5.37), (0.093, 0, 0.861, 0, 0.053, 4.536), (0, 0.053, 2.447, -0.429, 0, 5.43),
            (0.119, 0, 3.363, 0, -0.053, 8.513), (0.119, 0, 3.363, 0, 0.053, 1.487), (0, 0.053, 3.972, 0.429, 0, 4.569), (0.123998, -0.00183957, 6.275, 0.000691208, 0.0629731, 7.716), (0, 0.053, 5.215, 0.167, 0, 6.483), (0.071, 0, 6.279, 0, 0.053, 5.298),
            (0, -0.053, 6.805, -0.238, 0, 3.714), (-0.121, 0, 5.941, 0, 0.053, 1.487)))
ifs2.przeksztalcenie(10000)
ifs2.rysuj()

ifs3 = IFS(((0.824074, 0.281428, -1.88229, -0.212346, 0.864198, -0.110607), (0.088272, 0.520988, 0.78536, -0.463889, -0.377778, 8.095795)), (0.8, 0.2))
ifs3.przeksztalcenie(10000)
ifs3.rysuj()


class Wektor3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, wektor):
        return Wektor3D(self.x + wektor.x, self.y + wektor.y, self.z + wektor.z)

    def __sub__(self, wektor):
        return Wektor3D(self.x - wektor.x, self.y - wektor.y, self.z - wektor.z)

    def __mul__(self, liczba):
        return Wektor3D(self.x * liczba, self.y * liczba, self.z * liczba)

    __rmul__ = __mul__

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def dlugosc(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def skalarny(self, wektor):
        return self.x * wektor.x + self.y * wektor.y + self.z * wektor.z

    def wektorowy(self, wektor):
        return Wektor3D(self.y * wektor.z - self.z * wektor.y, self.z * wektor.x - self.x * wektor.z, self.x * wektor.y - self.y * wektor.x)

    def mieszane(self, wektor1, wektor2):
        return self.wektorowy(wektor1).skalarny(wektor2)


wek1 = Wektor3D(1, 2, 3)
wek2 = Wektor3D(1, 1, 2)
wek3 = Wektor3D(2, 1, 1)

wek1 = wek1 + wek2

print(wek1)
print(wek2)

wek1 = wek1 - wek2

print(wek1)

wek1 = wek1 * 2

print(wek1, "Dlugosc:", wek1.dlugosc())
print(wek1, "*", wek2, "=", wek1.skalarny(wek2))
print(wek1, "x", wek2, "=", wek1.wektorowy(wek2))
print(wek1, "x", wek2, "*", wek3, "=", Wektor3D.mieszane(wek1, wek2, wek3))


def Strumien(B, S):
    return B.skalarny(S)


def Lorentza(q, E, v, B):
    return q * (E + v.wektorowy(B))


def Praca(q, E, v):
    return q * (E.skalarny(v))


print("Strumien", Strumien(wek1, wek2), "Sila Lorentza", Lorentza(1e-12, wek1, wek2, wek3), "Praca sily Lorentza", Praca(1e-12, wek1, wek2))
