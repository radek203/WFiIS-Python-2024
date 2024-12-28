import functools

f = lambda x: x + 3

print(f(10))

print("")
f = (lambda x=r: x * x for r in range(5))
for el in f:
    print(el())

print("")
f = lambda *x: sum(x)
print(f(*range(10)))

print(bin(13))
print(int('0b1101', 2))

print(bool([]))
print(bool([1]))

print(ord('a'))
print(chr(97))

print(complex(13, 3))

print(oct(13))
print(int('0o15', 8))

# Mozna nadpisac funkcje, a jak potem usuniemy to znowu mamy poprzednia funkcje
# print = 6
# x = print + 2
# del print

# print('ala', x, callable(print))

x = 2


def fun(a, b):
    c = a + b
    print(locals())
    print(globals())


fun(4, 5)

for i in range(3):
    locals()[f'a{i}'] = i
    globals()[f'b{i}'] = i
    exec(f'c{i}=i')

print(locals())
print(globals())

# Prze odwolanie do  slownika mozna tak zrobic, normalnie nieS
# exec('0a=3')
locals()['0a'] = 3

# all - sprawdza czy wszystkie wartosci prawdziwe
print(all(range(10)))
print(all(range(2, 10)))

# any - sprawdza czy jakakolwiek wartosc jest prawdziwa
print(any(range(10)))

m = map(lambda x: x ** 2, range(5))
print(list(m))

m = map(lambda x, y: x + y, range(5), range(5, 10))
print(list(m))

# zip - bierze wartosci z tymi samymi indeksami
z = zip(range(5), range(5, 7), range(0, 10, 2))

print(list(z))

print(list(filter(lambda x: x % 2, range(10))))
print(list(filter(None, range(5))))

s = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(s)
