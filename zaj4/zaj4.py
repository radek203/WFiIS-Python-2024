import collections
import random

s = {}
s = collections.defaultdict(int)
print(s[7])

s[7] = 3
print("1:", s)

# Zwraca to co pod kluczem 7, jezeli nie ma nic to None
w = s.setdefault(7, None)
print("2:", w)
print(s)

# Jezli nie ma to doda z ta wartoscia
w = s.setdefault(8, 15)
print("3:", w)
print(s)

s[9] += 1
print(s)

s = {}
# Mozna dodac liste i do niej dodawac
s.setdefault(7, []).append(3)
print(s)

s.setdefault(7, []).append(13)
print(s)

s.setdefault(8, {}).setdefault(3, 1)
print(s)

s.setdefault(8, {}).setdefault(13, []).append(1)
print(s)

# Mozna zrobic jak indeksy od 0 do 4, z wartoscia domyslna 3
s = dict.fromkeys(range(5), 3)
print(s)

s = dict((k, f'{k}') for k in range(5))
print(s)

s = {k: f'{k}' for k in range(5)}
print(s)
print(type(s))

s = {7: 13, 8: 15}
print(s.keys())
print(s.values())
print(s.items())

# del s[10]

# Jezeli klucza nie ma to None
print(s.get(10))
# Jezeli klucza nie ma to 0
print(s.get(10, 0))

# s.pop(10)
s.pop(10, 0)

s.clear()

s1 = {'k1': 's1', 'k2': 's1', 'k3': 's1', 'k4': 's1'}
s2 = {'k1': 's2', 'k2': 's2', 'k3': 's2', 'k4': 's2'}
s1.update(s2)
print(s1)

s1 = {'k1': 's1', 'k2': 's1', 'k3': 's1', 'k4': 's1'}
# | zwraca nowy obiekt
print(s2 | s1)

# randint - przedzial domkniety obustronnie
print(random.randint(1, 100))

print(random.random())

# Do ascii i na odwrot
print(ord(chr(13)))

r = random.getrandbits(5)
print(r)
r = bin(r)
print(r, type(r))
r = int(r, 2)
print(r)

x = [1, 2, 3, 4, 5]
print(random.seed())
# print(random.getstate())
print(random.shuffle(x))
print(random.choice(x))
print(random.sample(x, 3))
print(random.choices(x, k=2))
