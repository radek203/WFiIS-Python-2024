import glob
import string

import matplotlib.pyplot as plt
import numpy


# Zadanie 1


def fun(filename, n):
    with open(filename) as f:
        lines = f.readlines()

        print("n poczatkowych wierszy:", lines[:n])
        print("n koncowych wierszy:", lines[-n:])
        print("co n-ty wiersz:", lines[::n])
        print("n-te slowo z kazdego wiersza", [ls[n] for line in lines if len(ls := line.split(" ")) >= n])
        print("n-ty znak z kazdego wiersza", [line[n] for line in lines if len(line) >= n])


fun('test.txt', 3)

# Zadanie 2
dane_wiersze = {}
for filename in glob.iglob('data/data*.in'):
    with open(filename) as f:
        linie = f.readlines()
        for i, linia in enumerate(linie):
            dane_wiersze.setdefault(i, []).append(float(linia))

# Format taki jak np. lubi excel (;)
with open('data.out', 'w') as f:
    for k, v in dane_wiersze.items():
        f.write(f"{k};{numpy.average(v)};{numpy.std(v)}\n")

# Zadanie 3
skrypt = """import glob
import matplotlib.pyplot as plt

# Musimy powtorzyc jezeli chcemy zeby skrypt dzialal niezaleznie
dane_wiersze = {}
for filename in glob.iglob('data*.in'):
    with open(filename) as f:
        linie = f.readlines()
        for i,linia in enumerate(linie):
            dane_wiersze.setdefault(i, []).append(float(linia))

numery = []
srednie = []
odchylenia = []
with open('data.out', 'r') as in_file:
    for line in in_file:
        line = line.split(";")
        numery.append(int(line[0]))
        srednie.append(float(line[1]))
        odchylenia.append(float(line[2]))

for k,v in dane_wiersze.items():
    for point in v:
        plt.plot(k, point, 'o')
plt.errorbar(numery, srednie, marker="*", yerr=odchylenia)

plt.title('Srednia dla danego wiersza')
plt.xlabel('Wiersz')
plt.ylabel('Srednia')
plt.show()"""

with open('skrypt.py', 'w') as f:
    f.write(skrypt)

# Zadanie 4

dane = {}
for filename in glob.iglob('rank/*.txt'):
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            line = line.strip().split(" ")
            dane.setdefault(line[0], {}).setdefault(filename[5:9], line[1])

with open("rank.out", "w") as f:
    f.write(f"{'Nazwisko':<9}")
    for rok in range(2000, 2021):
        f.write(f"{rok:<5}")
    f.write("\n")
    for k, v in sorted(dane.items()):
        f.write(f"{k:<9}")
        for rok in range(2000, 2021):
            rok = str(rok)
            if rok in v:
                f.write(f"{v[rok]:<5}")
            else:
                f.write(f"{'-':<5}")
        f.write("\n")


# Zadanie 5
def wykres(letters, alfabetycznie=True):
    if not alfabetycznie:
        letters = dict(reversed(sorted(letters.items(), key=lambda x: x[1])))
    plt.bar(letters.keys(), letters.values())
    plt.title('Ilosc danych slow na dana litere')
    plt.xlabel('Litery')
    plt.ylabel('Ilosc wystapien slow')
    plt.show()


for filename in glob.iglob('zad5*.in'):
    with open(filename) as f:
        letters = {}
        for letter in string.ascii_lowercase:
            letters[letter] = 0
        for line in f.readlines():
            for slowo in line.lower().split(" "):
                if slowo[0] in letters:
                    letters[slowo[0]] += 1
        wykres(letters, False)
