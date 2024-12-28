import math
import random

# Zadanie 1
print("\nZadanie 1")


def naturalne():
    x = 0
    while True:
        yield x
        x += 1


def doskonale(sek):
    for i in sek:
        if i == sum(j for j in range(1, i) if i % j == 0):
            yield i


def spr(sek, maks):
    for i in sek:
        if i > maks:
            break
        yield i


g = naturalne()
ggg = spr(g, 10000)
gg = doskonale(ggg)
print(list(gg))

# Zadanie 2
print("\nZadanie 2")


def gen(a, max_x):
    i = 1
    u_i = 0
    x_i = 1
    while True:
        u_i = u_i + (a / x_i)
        x_i = 1 + i * a
        if x_i > max_x:
            break
        yield u_i, x_i, math.log(x_i)
        i += 1


for i in gen(0.05, 1.5):
    print(i)

# Zadanie 3
print("\nZadanie 3")


def sinus(x):
    k = 0
    while True:
        yield (((-1) ** k) / math.factorial(1 + 2 * k)) * (x ** (1 + 2 * k))
        k += 1


w = math.pi
s = sinus(w)
porownanie = math.fabs(math.sin(w))

suma = 0
i = 0
# Do 100, taki ogranicznik
for i in range(1, 100):
    suma += next(s)
    if math.fabs(suma) <= (porownanie + 10e-8):
        break

print("Funkcja potrzebowala", i, "iteracji ", suma)

# Zadanie 4
print("\nZadanie 4")


def customrange(mini=0, maxi=None, krok=1.0):
    if krok == 0:
        raise ValueError
    if maxi is None:
        maxi = mini
        mini = 0
    while True:
        if (krok > 0 and mini >= maxi) or (krok < 0 and mini <= maxi):
            break
        yield float(mini)
        mini += krok


print("Range: ", list(range(10)))
print("Custom Range: ", list(customrange(10)))

print("Range: ", list(range(-10)))
print("Custom Range: ", list(customrange(-10)))

print("Range: ", list(range(1, 10)))
print("Custom Range: ", list(customrange(1, 10)))

print("Range: ", list(range(10, 1)))
print("Custom Range: ", list(customrange(10, 1)))

print("Range: ", list(range(1, 10, 2)))
print("Custom Range: ", list(customrange(1, 10, 2)))

print("Range: ", list(range(1, 10, -2)))
print("Custom Range: ", list(customrange(1, 10, -2)))

print("Range: ", list(range(10, 1, 2)))
print("Custom Range: ", list(customrange(10, 1, 2)))

print("Range: ", list(range(10, 1, -2)))
print("Custom Range: ", list(customrange(10, 1, -2)))

print("Custom Range: ", list(customrange(10, 1, -1.2)))


# Zadanie 5


def losowanie(liczba=1):
    while liczba >= 0.1:
        nowa = random.uniform(liczba - 0.4, liczba - 1) if random.randint(0, 1) else random.uniform(liczba + 0.4, liczba + 1)
        yield nowa
        liczba = nowa


for i in losowanie(2):
    print(i)
