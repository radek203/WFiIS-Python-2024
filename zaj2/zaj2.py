import copy

k = [8, 0, 17, 1, 10, 13, 19, 13, 10, [4, 5, 6]]
print(k)

# Plytka kopia (wskaznik)
c = k
print(c, k)
print(id(c), id(k))
c[0] = 2
print(c, k)

# Ale mamy modyfikowalny element listy, srednio pomaga
c = k[:]
print(c, k)
print(id(c), id(k))

c[-1][1] = 7
print(c, k)
print(id(c), id(k))

# Dalej nic nie daje
c = k.copy()
c[-1][0] = 10
print(c, k)
print(id(c), id(k))

# Dalej nic
c = copy.copy(k)
c[-1][2] = 99
print(c, k)
print(id(c), id(k))

# Gleboka kopia, w koncu dziala
c = copy.deepcopy(k)
c[-1][2] = 123
print(c, k)
print(id(c), id(k))

k = [8, 0, 17, 1, 10, 13, 19, 13, 10, [4, 5, 6]]
print(k.count(13))
print(k.count(-13))

print(k.index(13))
# print(k.index(-13))

print(13 in k)
print(13 not in k)
print(k)
k.insert(4, -13)
print(k)
# Jak wychodzi po za poczatek to wstawiamy na poczatek
k.insert(-23, 4)
print(k)
# Jak wcyhodzi po za koniec to wstawiamy na koniec
k.insert(23, 4)
print(k)

k[1:4] = [7, 8, 9, 10, ]
print(k)

k[1:4] = [[7, 8, ], ]
print(k)

# Usuwa element
k.remove(1)
print(k)

# Usuwa indeks
del k[3]
print(k)

# Usuwa ostatni i go zwraca
print(k.pop())
print(k)

# Usuwa wedlug indeksu i go zwraca
print(k.pop(-3))
print(k)

k = [1, 2] * 10
# Zmieniamy tylko ta 1 wartosc (Obiekt niemodyfikowalny)
k[2] += 1
print(k)

k = [[]] * 10
print(k)
# Zmieniamy wszystkie wartosci (Obiekt modyfikowalny - stworzona 1 lista i skopiowana 10 razy)
k[3].append(1)
print(k)

# range(10) - od 0 do 9 wlacznie
k = [[] for i in range(10)]
# Zmieni tylko ta jedna
k[3].append(1)
print(k)

# Pojedynczy obiekt
k[3].append([5, 6, 7])
# ...wszystkie po kolei dodajemy, (obiekt iterowalny)
k[3].extend([5, 6, 7])
print(k)

k[3].extend('1,2,3')
print(k)

k = []
for i in range(10):
    k.append(i)
print(k)
k = list(range(20))
print(k)
k = list(range(3, 10))
print(k)
k = list(range(3, 10, 2))
print(k)
k = list(range(10, 0, -1))
print(k)
k = list(range(10, 0, 1))
print(k)
k = [i for i in range(10)]
print(k)

k = [8, 0, 17, 1, 10, 13, 19, 13, 10, 3, ]
for i in k:
    i *= 2
    print(i, end=', ')

print('\n', k)

for i in range(len(k)):
    k[i] *= 2

print(k)

# i - index, v - wartosc
for i, v in enumerate(k):
    k[i] = 1 if v > 0 else -1
print(k)

k = [8, 0, 17, 1, 10, 13, 19, 13, 10, 3, ]
for i in k:
    if i % 2:
        break
else:
    print('???')

np = [i for i in k if i % 2]
print(np)
np = [1 if i > 0 else -1 for i in k]
print(np)

k = [(k[i], k[-i - 1]) for i in range(len(k) // 2)]
print(k)

for i, j in k:
    print(i, j)

N = 3
k = []
for i in range(N):
    tmp = []
    for j in range(N):
        tmp.append((i, j))
    k.append(tmp)
print(k)

k, tmp = [], []
for i in range(N):
    for j in range(N):
        tmp.append((i, j))
    # Caly czas ten sam obiekt
    k.append(tmp)
    tmp.clear()
print(k)

k = [[(i, j) for j in range(N)] for i in range(N)]
print(k)

k = [(89, 34), (92, 31), (96, 0), (48, 30), (38, 10), ]
c = k[:]
c.sort()  # c = c.sort() - nie! (zwroci None - funkcja void)
print("Posortowane:", c)

c = k[:]
# Sortujemy wzgledem 2 elementu
c.sort(key=lambda x: x[1])
print(c)

c = k[:]
# Odwaracamy sortowanie (ale dalej wedlug 1 elementu)
c.sort(reverse=True)
print(c)

c = k[:]
for i, j in sorted(k):
    print(i, j)
print(c)

c = k[:]
c.reverse()
print(c)

c = k[::-1]
print(c)
