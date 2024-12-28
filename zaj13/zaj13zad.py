import collections
import dataclasses
import json
import os
import random


class Stos:
    def __init__(self, *args):
        if len(args) == 1:
            self.stos = []
            match args[0]:
                case list():
                    print("TEST1")
                    for el in args[0]:
                        self.stos.append(el)
                case Stos():
                    print("TEST2")
                    for el in args[0].stos:
                        self.stos.append(el)
                case _:
                    print("TEST3")
                    self.stos.append(args[0])
        else:
            print("TEST4")
            self.stos = list(args)

    def dodaj(self, val):
        self.stos.append(val)

    def wypisz(self):
        print(self.stos)


class SortedStos(Stos):
    def __init__(self, *args):
        Stos.__init__(self, *args)

        cnt = collections.Counter(map(lambda elem: type(elem).__name__, self.stos))
        nowy = filter(lambda elem: type(elem).__name__ == cnt.most_common(1)[0][0], self.stos)

        self.stos = list(nowy)
        self.stos.sort()

    def dodajJesli(self, val):
        if val > self.stos[-1]:
            self.stos.append(val)


s1 = SortedStos()
for i in range(100):
    s1 = SortedStos([random.randint(0, 100) for _ in range(100)])
    print(len(s1.stos))


@dataclasses.dataclass
class Pracownik:
    nazwisko: str
    imie: str
    wiek: int
    wyksztalcenie: str


@dataclasses.dataclass
class Oferta:
    opis: str
    wiek: int
    wyksztalcenie: str


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


def loadOsoby():
    lista_osob = []
    while input("Dodac nastepnego") == "true":
        nazw = input("Podaj nazwisko")
        im = input("Podaj imie")
        wi = int(input("Podaj wiek"))
        wyksz = input("Podaj wyksztalcenie")
        lista_osob.append(Pracownik(nazw, im, wi, wyksz))
    if os.path.isfile("osoby.json"):
        f = open("osoby.json", "r")
        lista_osob_load = json.load(f)
        for el in lista_osob_load:
            lista_osob.append(el)
    f = open("osoby.json", "w")
    json.dump(lista_osob, f, cls=EnhancedJSONEncoder)
    return lista_osob


def loadOferty():
    lista_ofert = []
    while input("Dodac nastepna") == "true":
        nazw = input("Podaj opis")
        wi = int(input("Podaj wiek"))
        wyksz = input("Podaj wyksztalcenie")
        lista_ofert.append(Oferta(nazw, wi, wyksz))
    if os.path.isfile("oferty.json"):
        f = open("oferty.json", "r")
        lista_ofert_load = json.load(f)
        for el in lista_ofert_load:
            lista_ofert.append(el)
    f = open("oferty.json", "w")
    json.dump(lista_ofert, f, cls=EnhancedJSONEncoder)
    return lista_ofert


def szukaj(pracownicy, oferty):
    pasujace = []
    for off in oferty:
        for pr in pracownicy:
            if off['wiek'] == pr['wiek'] and off['wyksztalcenie'] == pr['wyksztalcenie']:
                pasujace.append((off, pr))
    print(pasujace)


oso = loadOsoby()
ofe = loadOferty()
szukaj(oso, ofe)
