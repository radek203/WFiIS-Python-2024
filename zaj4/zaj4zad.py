import copy
import random
import string

# 1
print("Zadanie 1")
k = random.randint(1, 10)
lista = [random.randrange(0, 5 * k) for i in range(k)]
lista_copy = copy.deepcopy(lista)
print("k:", k, lista)
ile_zostalo = {}
for i in range(100):
    random.shuffle(lista)
    ile = 0
    for j in range(k):
        if lista[j] == lista_copy[j]:
            ile += 1
    ile_zostalo.setdefault(ile, 0)
    ile_zostalo[ile] += 1
print(ile_zostalo)

# 2
print("Zadanie 2")
k = random.randint(1, 20)
losowy = random.sample(string.ascii_lowercase, k)
# losowy = [string.ascii_lowercase[random.randint(0, len(string.ascii_lowercase))] for i in range(k)]
# losowy = [chr(random.randint(97, 122)) for i in range(k)]
print("k:", k, ".".join(losowy))

# 3
print("Zadanie 3a")
losowe = [random.randrange(0, 20) for i in range(100)]
print(losowe)
losowe_sl = {}
for i, v in enumerate(losowe):
    losowe_sl.setdefault(v, []).append(i)
print(losowe_sl)

print("Zadanie 3b")
losowe_sl2 = {}
# lastIndex = 0
for v in losowe:
    # losowe_sl2.setdefault(v, []).append(lastIndex := losowe.index(v, lastIndex))
    losowe_sl2.setdefault(v, []).append(losowe.index(v, losowe_sl2[v][-1] + 1 if losowe_sl2[v] else 0))
print(losowe_sl2)

# 4
print("Zadanie 4")
# Mozna zrobic przez :=
result = {n: sum((num := str(random.randint(10 ** (n - 1), 10 ** n - 1))) == num[::-1] for _ in range(1000)) for n in range(3, 7)}
print(result)

# 5
print("Zadanie 5")
slownik1 = {i: random.randrange(1, 100) for i in range(10)}
slownik2 = {i: random.randrange(1, 100) for i in range(10)}
print(slownik1)
print(slownik2)
slownik1 = {v: k for k, v in slownik1.items()}
slownik2 = {v: k for k, v in slownik2.items()}
print(slownik1)
print(slownik2)
nowy_slownik = {i: (slownik1[i], slownik2[i]) for i in slownik1 if i in slownik2}
print("NOWY:", nowy_slownik)
