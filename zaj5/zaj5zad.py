import math
import random
# import sys
import string


def zad1(f1c):
    stale = [x for x in f1c if x in string.ascii_lowercase and x != 'x']
    print(stale)
    f2 = [str(random.randint(0, 9)) for _ in stale]
    f2 = "".join(f2)
    tr = str.maketrans("".join(stale), f2)
    print("f2: " + f2, "tr:", tr)
    f1c = f1c.translate(tr)
    print(f1c)

    krotki = [(x := random.uniform(0, 1), eval(f1c)) for _ in range(10)]

    return krotki


# print(zad1(sys.argv[1]))


def zad2(*a):
    ilosc = {}
    for lis in a:
        for i in lis:
            x = ilosc.setdefault(i, 0)
            ilosc[i] = x + 1
    print(ilosc)

    wynik = []
    for k, w in ilosc.items():
        if w == len(a):
            wynik.append(k)
    return wynik


powt = zad2([1, 2, 3, 5], [3, 4, 5], [3, 5, 6, 7])
print(powt)


def zad3(a, b, c=True):
    lista = [(a[k1], b[k1]) for k1 in a if k1 in b]

    kr = min(len(a), len(b))
    if c and not len(lista) == kr:
        lista.extend([(None, None) for _ in range(kr - len(lista))])

    return lista


li = zad3({'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'e': 2})
print(li)


# Zadanie 4


def zad4(n):
    d = {(0, 0): 1}

    for i in range(n + 1):
        for j in range(n + 1):
            if i == j:
                d[(i, j)] = 0

    for i in range(n + 1):
        d[(i, 0)] = 1

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            d[(j, i)] = (i + 1) * d[(j - 1), i] + (j - i) * d[(j - 1, i - 1)]

    print(d)


zad4(9)

print("Zadanie 5")


def zad5(w, a, b, sposob='r'):
    kroki = 0
    if sposob == 'r':
        x = a - 1
        while x != w:
            kroki += 1
            x = random.randint(a, b)
            a, b = ((a + 1), b) if x < w and x != w else (a, (b - 1))
    else:
        while a <= b:
            kroki += 1
            x = math.floor((a + b) / 2)
            a, b = (x + 1, b) if x < w and x != w else (a, x - 1)

    print("Ilosc krokow: ", kroki)


zad5(4, 1, 10)
zad5(4, 1, 10, 'n')
