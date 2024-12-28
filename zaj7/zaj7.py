import random


def gen():
    x = 1
    yield x
    x += 2
    yield x
    x += 2
    yield x


for i in gen():
    print(i)


def gene(seq, f):
    for el in seq:
        yield f(el)


print("TEST")
w = (random.randrange(50) for _ in range(10))
for i in gene(w, lambda x: x ** 3):
    print(i)


def gener(seq, f):
    yield from map(f, seq)


def genera(seq, f):
    for el in seq:
        if el > 20:
            return 'blad'
        yield f(el)


print("TEST")
w = [9, 5, 31, 7, 28, 36]
for i in genera(w, lambda x: x ** 3):
    print(i)

g = genera(w, lambda x: x ** 3)


# while 1:
#    print(next(g))


def generat(seq, f):
    while True:
        x = yield
        yield f(seq + x)


gg = generat('Ala ma kota', lambda s: s.title())
next(gg)
print(gg.send('?'))
next(gg)
print(gg.send('!'))
