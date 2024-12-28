import sys

# 1
if len(sys.argv) < 2:
    print("Musisz podac wiecej parametrow")
    exit(0)

napis = ''.join(sys.argv[1:])

print(napis)

# 2
small_letters = []
big_letters = []
digits = []
not_letters = []
for s in napis:
    if s.islower():
        small_letters.append(s)
    elif s.isupper():
        big_letters.append(s)
    elif s.isdigit():
        digits.append(s)
    if not s.isalpha():
        not_letters.append(s)

print(small_letters)
print(big_letters)
print(digits)
print(not_letters)

# 3
small_letters_2 = []
for i in small_letters:
    if i not in small_letters_2:
        small_letters_2.append(i)

krotnosci = [(i, small_letters.count(i)) for i in small_letters_2]

print(small_letters_2)
print(krotnosci)

# 4
print(sorted(krotnosci, reverse=True, key=lambda x: x[1]))
print(krotnosci)

# 5
samogloski = 'aeiyou'
samoglosek = 0
for i in napis:
    if i.lower() in samogloski:
        samoglosek += 1

print(samoglosek)
spolglosek = len(napis) - samoglosek - len(not_letters)
print(spolglosek)

jakies_krotki = [(int(i), samoglosek * int(i) + spolglosek) for i in digits]
print(jakies_krotki)

# 6

suma_x = 0
suma_y = 0
for i in jakies_krotki:
    suma_x += i[0]
    suma_y += i[1]

avg_x = suma_x / len(jakies_krotki)
print("AVG_X = ", avg_x)
avg_y = suma_y / len(jakies_krotki)
print("AVG_Y = ", avg_y)

d = sum((i[0] - avg_x) ** 2 for i in jakies_krotki)

suma = sum((x - avg_x) * y for x, y in jakies_krotki)

a = suma / d

print("D = ", d)
print("a = ", a)

b = avg_y - a * avg_x
print("b = ", b)
print(f"y={a}x+{b}")
