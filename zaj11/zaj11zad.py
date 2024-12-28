import abc
import math


class Pierwsze1:
    def __init__(self, a, b):
        self.x = a - 1
        self.b = b

    def __iter__(self):
        return self

    def __next__(self):
        self.x += 1
        while self.x < self.b:
            if self.czyLiczbaPierwsza():
                return self.x
            self.x += 1
        raise StopIteration

    def czyLiczbaPierwsza(self):
        if self.x <= 1:
            return False
        liczba = 2
        while liczba < math.sqrt(self.x) + 1:
            if self.x % liczba == 0:
                return False
            liczba += 1
        return True


class Pierwsze2:
    def __init__(self, a, b):
        self.x = a - 1
        self.b = b

    def __iter__(self):
        return Pierwsze2(self.x, self.b)

    def __next__(self):
        self.x += 1
        while self.x < self.b:
            if self.czyLiczbaPierwsza():
                return self.x
            self.x += 1
        raise StopIteration

    def czyLiczbaPierwsza(self):
        if self.x <= 1:
            return False
        liczba = 2
        while liczba < math.sqrt(self.x) + 1:
            if self.x % liczba == 0:
                return False
            liczba += 1
        return True


p1 = Pierwsze1(0, 20)
for i in p1:
    print(i)

p2 = Pierwsze2(0, 20)
for i in p2:
    for j in p2:
        print(i, j)


class Automat(abc.ABC):
    @abc.abstractmethod
    def __iter__(self):
        pass

    @abc.abstractmethod
    def __next__(self):
        pass


class AutomatPochodna1D(Automat):
    def __init__(self, regula, start, iteracji):
        self.regula = regula
        self.stan = start
        self.wartosci = self.reguly(regula)
        self.N = len(start)
        self.iteracji = iteracji
        self.iteracji_teraz = 0

    def reguly(self, regula):
        binarnie = f"{regula:08b}"
        wartosci = {}
        kombinacje = [
            (1, 1, 1),
            (1, 1, 0),
            (1, 0, 1),
            (1, 0, 0),
            (0, 1, 1),
            (0, 1, 0),
            (0, 0, 1),
            (0, 0, 0)
        ]
        for i, kombinacja in enumerate(kombinacje):
            wartosci[kombinacja] = int(binarnie[i])
        print(wartosci)
        return wartosci

    def sasiedzi(self, index):
        left = self.stan[(index - 1) % self.N]
        center = self.stan[index]
        right = self.stan[(index + 1) % self.N]
        return left, center, right

    def __iter__(self):
        return self

    def __next__(self):
        self.iteracji_teraz += 1
        if self.iteracji_teraz >= self.iteracji:
            raise StopIteration
        nowy_stan = []
        for i in range(self.N):
            trojka = self.sasiedzi(i)
            nowy_stan.append(self.wartosci[trojka])
        self.stan = nowy_stan
        return self.stan


stanPoczatkowy = [0] * 31
stanPoczatkowy[len(stanPoczatkowy) // 2] = 1
for i in AutomatPochodna1D(182, stanPoczatkowy, 16):
    for j in i:
        if j == 1:
            print("*", end='')
        else:
            print(" ", end='')
    print("")


class AutomatPochodna2D(Automat):
    def __init__(self, N, bok):
        self.stan = [[] for _ in range(N)]
        offset = (N // 2) - (bok // 2)
        for i in range(N):
            for j in range(N):
                self.stan[i].append(0)
        for i in range(offset, N - offset + (1 if bok % 2 else 0)):
            for j in range(offset, N - offset + (1 if bok % 2 else 0)):
                self.stan[i][j] = 1
        self.N = N
        for wiersz in self.stan:
            for wartosc in wiersz:
                if wartosc == 1:
                    print("*", end='')
                else:
                    print(" ", end='')
            print("")

    def sasiedzi(self, indexX, indexY):
        # Wymaga refaktoryzacji
        elementy = [self.stan[(indexX - 1) % self.N][(indexY - 1) % self.N],
                    self.stan[(indexX - 1) % self.N][indexY % self.N],
                    self.stan[(indexX - 1) % self.N][(indexY + 1) % self.N],
                    self.stan[indexX % self.N][(indexY - 1) % self.N],
                    self.stan[indexX % self.N][(indexY + 1) % self.N],
                    self.stan[(indexX + 1) % self.N][(indexY - 1) % self.N],
                    self.stan[(indexX + 1) % self.N][indexY % self.N],
                    self.stan[(indexX + 1) % self.N][(indexY + 1) % self.N]]
        return sum(elementy)

    def __iter__(self):
        return self

    def __next__(self):
        nowy_stan = [[] for _ in range(self.N)]
        for i in range(self.N):
            for j in range(self.N):
                sasiedzi = self.sasiedzi(i, j)
                if self.stan[i][j] == 0 and sasiedzi == 3:
                    nowy_stan[i].append(1)
                elif self.stan[i][j] == 0:
                    nowy_stan[i].append(0)
                if self.stan[i][j] == 1 and (sasiedzi == 3 or sasiedzi == 2):
                    nowy_stan[i].append(1)
                elif self.stan[i][j] == 1:
                    nowy_stan[i].append(0)
        self.stan = nowy_stan
        return self.stan


p2 = AutomatPochodna2D(20, 11)
for _ in range(5):
    for wiersz in next(p2):
        for wartosc in wiersz:
            if wartosc == 1:
                print("*", end='')
            else:
                print(" ", end='')
        print("")
