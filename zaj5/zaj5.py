import random


def fun(a, *b, c=3, **d):
    pass


def suma(a, b):
    return a + b


def podziel(a, b):
    return a / b


def funn(a, *b):
    print(a, b)


def potega(a, b=2):
    return a ** b


def func(**d):
    print(d)


def funcc(a, /, *b, c=4, **d):
    print(a, b, c, d)


print(suma(8, 1))
print(podziel(b=1, a=3))
print(funn(1, 3, 6, 7))
print(potega(3))
func()
func(a=1, b=2, c=3)
fun(1, 2, 3, c=2, b=3, d=4, e=5)


def test(a=1, b=2):
    print(a, b)


test(b=1)


# Nie tworzy nowej list za kazdym razem, tak samo slownik
def fun(el, p=[]):
    p.append(el)
    print(p)


fun(3)
fun(1)


# Liste i slownik zmieni
def fun(n, li, s, sl):
    n = 3
    li[1] = 3
    s = '3'
    sl[1] = 3


zn = 1
zl = [1, 2, 3, 4]
zs = '1'
zd = {1: 1, 2: 2, 3: 3, 4: 4}

fun(zn, zl, zs, zd)
print(zn, zl, zs, zd)

print(isinstance(1, int))
print(isinstance(1, (int, float)))
print(isinstance(1, float))
print(isinstance(1., (int, float)))


def fun(n):
    res = [a for _ in range(n) if (a := random.randrange(100)) % 2]
    return res, min(res), max(res)


np, wmin, wmax = fun(20)
print(np, wmin, wmax)


def fun():
    pass


x = 7


def funcccc(p):
    y = x + p
    return y


print(':', funcccc(3))


def funcccc2(p):
    y = x + p
    return y


# def funcccc3(p):
#     y = x+p
#     x = x - 1
#     return y


def funcccc4(p):
    global x
    y = x + p
    x = 5
    return y


print(funcccc4(3))
print(x)

eval('2+7')
x = 4
eval('2+x+7')
