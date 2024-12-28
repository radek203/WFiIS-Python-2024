import math
import random
import sys
import time

powt = 1000
N = 10000


def forStatement():
    # Dodawanie elementu
    li = []
    for i in range(N):
        li.append(i)
    # Dodawanie elementu podniesionego do kwadratu
    li = []
    for i in range(N):
        li.append(i ** 2)
    # Sumowanie elementow for
    suma = 0
    for i in li:
        suma += i
    # Sumowanie elementow sum
    suma = sum(li)
    # Konwersja map do listy
    m = map(lambda x: x, range(N))
    li = []
    for i in m:
        li.append(i)
    # Konwersja generatora do listy
    g = (i for i in range(N))
    li = []
    for i in g:
        li.append(i)


def listComprehension():
    # Dodawanie elementu
    li = [i for i in range(N)]
    # Dodawanie elementu podniesionego do kwadratu
    li = [i ** 2 for i in range(N)]
    # Sumowanie elementow for
    suma = 0
    for i in li:
        suma += i
    # Sumowanie elementow sum
    suma = sum(li)
    # Konwersja map do listy
    m = map(lambda x: x, range(N))
    li2 = [i for i in m]
    # Konwersja generatora do listy
    g = (i for i in range(N))
    li3 = [i for i in g]


def mapFunction():
    # Dodawanie elementu
    m = map(lambda x: x, range(N))
    # Dodawanie elementu podniesionego do kwadratu
    m = map(lambda x: x ** 2, range(N))
    # Sumowanie elementow for
    suma = 0
    for i in m:
        suma += i
    # Sumowanie elementow sum
    suma = sum(m)
    # Konwersja map do listy
    m = list(m)
    # Konwersja generatora do listy
    g = (i for i in range(N))
    g = list(g)


def generatorExpression():
    # Dodawanie elementu
    g = (x for x in range(N))
    # Dodawanie elementu podniesionego do kwadratu
    g = (x ** 2 for x in range(N))
    # Sumowanie elementow for
    suma = 0
    for i in g:
        suma += i
    # Sumowanie elementow sum
    suma = sum(g)
    # Konwersja map do listy
    m = map(lambda x: x, range(N))
    m = list(m)
    # Konwersja generatora do listy
    g = list(g)


def tester(f):
    t = time.time_ns()
    for _ in range(powt):
        f()
    return time.time_ns() - t


print(sys.version, time.time_ns())
test = (forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

# Zadanie 2
print("")
print("ZADANIE 2")

promien = 1
punktow = 100000
bok = 2
pole_kwadratu = bok * bok
# Z tego wychodzi pole kola = pi
# pole_kola = math.pi * promien**2
points = ((random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(0, punktow))
w_srodku = list(filter(lambda punkt: punkt[0] ** 2 + punkt[1] ** 2 <= promien, points))
# print(pole_kola/pole_kwadratu)
print("PI: ", (len(w_srodku) / punktow) * pole_kwadratu)

# Zadanie 3
print("")
print("ZADANIE 3")


def funkcja(x, y):
    n = len(x)

    x_srednia = sum(x) / n
    y_srednia = sum(y) / n

    d = sum(map(lambda x_i: (x_i - x_srednia) ** 2, x))

    a = sum(map(lambda x_i, y_i: (y_i * (x_i - x_srednia)), x, y)) / d
    b = y_srednia - a * x_srednia

    delta_y = math.sqrt(sum(map(lambda x_i, y_i: (y_i - (a * x_i + b)) ** 2, x, y)) / n)
    delta_a = delta_y / math.sqrt(d)

    delta_b = delta_y * math.sqrt((1 / n) + ((x_srednia ** 2) / d))

    return a, b, delta_a, delta_b


x = [1, 2, 3]
y = [2, 4, 6]

wyniki = funkcja(x, y)

if wyniki[0] == 2 and wyniki[1] == 0 and wyniki[2] == 0 and wyniki[3] == 0:
    print("Poprawnie", wyniki)

x = [1, 2, 3]
y = [2, 6, 11]

print(funkcja(x, y))

# Zadanie 4
print("")
print("ZADANIE 4")


def myreduce(f, sek):
    elem = sek[0]

    for el in sek[1:]:
        elem = f(el, elem)

    return elem


print(myreduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
print(myreduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))

# Zadanie 5
print("")
print("ZADANIE 5")

macierz = [
    [2, 9, 6],
    [6, 5, 7],
    [4, 6, 8]
]

macierz2 = [
    [2, 9, 6],
    [6, 5, 7],
    [4, 6, 8]
]

macierz3 = [
    [2, 9, 6],
    [6, 5, 7],
    [4, 6, 8]
]

print(list(map(lambda row: max(row), macierz)))
print(list(map(lambda row: max(row), zip(*macierz))))
print(myreduce(lambda m1, m2: [[w1 + w2 for w1, w2 in zip(row1, row2)] for row1, row2 in zip(m1, m2)], [macierz, macierz2, macierz3]))
