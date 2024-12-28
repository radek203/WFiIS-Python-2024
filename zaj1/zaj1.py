#!/usr/bin/env python3.11
# Komenda wazniejsza -> np. python3 zaj1.py (Jak jest 1 wersja w systemie, nie ma znaczenia,
# i tak lepiej napisać -> oznaczamy wersje na ktorej na pewno dziala

# lepiej importowac cale moduly niz tylko dane komendy
import math
import sys

# from cmath import sqrt as csqrt

# Program glowny i tak ma nazwe main chcociaz nie wywolujemy bezposrednio main() {} itd.

# '' "" ''' - wszystko to, to 'str'

# ''' - to nie jest komentarz tylko utworzony string - i nie przypisany do zadnej zmiennej

x = '''
TEST
'''

print(x)
print('Hello')
print("HELLO")
print('''HELLO''')


# Jezeli funkcja jawnie nie zwraca nic to zwraca None
def fun(x):
    x


def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)


y = fun(2)
print(y)
print(type(y))

# liczba = input("Podaj liczbe: ")
result = factorial(int("2"))
print("Wynik:", result)
print(type(result))

# Uzyskujemy informacje o funkcjach w module, albo dla obiektu
# dir(math)

# Uzyskujemy informacje o funkcji
# help(math.sinh)

# Nie ma double, jest float - ale jest to podwojna precyzja
a = 1.5
print(a)
print(type(a))

# Tuple - nie jest mutable
b = 1, 3, 5
print(b)

# * - nie jest wskaznikiem, tylko tworzy liste - jest mutable
c, *d = a, b, 99
print(" ", c, " ", d)

print(1 / 2, 1 // 2)
print(1. / 2, 1. // 2)

# ** - potegowanie, 3 arg w pow to modulo
print(2 ** 4, pow(2, 6, 2), math.pow(2, 4))
print(round(1 / 3, 3))

# Zwraca to co przed , i po , z liczby
t = math.modf(5 / 3)
print(t[0], t[1])

print(abs(-1.7), math.fabs(-1.7))
# abs zwraca tego samego typu co podalismy
print(abs(-2), math.fabs(-2))

if True:
    pass
elif False:
    pass
else:
    pass

a = "X" if 10 > 5 else "Y"

print("")
while True:
    try:
        a = float(input("Podaj a: "))
        b = float(input("Podaj b: "))
        c = float(input("Podaj c: "))
    except ValueError:
        print("Musisz podac liczbe!")
    else:
        # Przypisujemy, potem porownujemy dlatego tez potrzebny nawias
        if (delta := b ** 2 - 4 * a * c) > 1e-6:
            deltaS = math.sqrt(delta)
            x1 = (-b - deltaS) / (2 * a)
            x2 = (-b + deltaS) / (2 * a)
            print(f'x1={x1:.3f}', f'x1={x2:.3f}')
        elif abs(delta) <= 1e-6:
            x = -b / (2 * a)
            print(f'x1=x2={x:.3f}')
        else:
            print("Brak rozwiazan rzeczywistych")
        break

if len(sys.argv) != 5:
    sys.exit()

print("")
print(type(sys.argv))
print(len(sys.argv))
print(sys.argv[0])
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

eps = float(sys.argv[4])

# To jest pusta tuple
k = ()
print(type(k))
# To jest tylko int
k = (2)
print(type(k))
# To jest tuple
k = (2,)
print(type(k))

a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)

k = (1, 2.4, "aaa", (4, 3, 2, 1), [1, 2, 3], True, None,)
print(len(k))
print(k[-1])
print(k[::-1])
print(k[:2:-1])
k[4][0] = 5
print(k)

k = []
print(type(k))
k = [2]
print(type(k))
k = [2, 5]
print(type(k))

k[0] = k
k.append(k)
print(k)
print(k[0])

print(bool([]))
print(bool(None))
print(bool(False))

str = "xppaaaaaaaa"
print(str[::-1])
