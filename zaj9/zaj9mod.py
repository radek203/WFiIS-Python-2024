import datetime


def val_card_number(card):
    """
    Funkcja sprawdza poprawnosc numeru karty wykorzystujac algorytm Luhna

    :raise ValueError
    :param card: Numer karty do sprawdzenia
    :return: bezposrednio nie zwracamy nic
    """
    nums = [int(num) for num in card[::-1]]
    if len(nums) != 16:
        raise ValueError("Nieprawidlowa dlugosc karty: " + card)
    suma = 0
    for i, v in enumerate(nums):
        if i % 2:
            suma += v * 2 if v * 2 < 10 else ((v * 2) // 10 + (v * 2) % 10)
        else:
            suma += v

    suma %= 10
    if suma != 0:
        raise ValueError("Nieprawidlowy numer karty: " + card)


def val_pesel(pesel, data_ur, plec):
    """
    Funkcja sprawdza poprawnosc numeru pesel

    :raise ValueError
    :param pesel: Numer pesel do sprawdzenia
    :param data_ur: Data urodzenia typu datetime.date
    :param plec: podzielne przez 2 - kobieta, jezeli nie mezczyzna
    :return: bezposrednio nie zwracamy nic
    """
    pesel_nums = [int(num) for num in pesel]
    if len(pesel_nums) != 11:
        raise ValueError("Nieprawidlowa dlugosc (!=11): " + pesel)
    if pesel[0:2] != str(data_ur.year)[2:4]:
        raise ValueError("Cyfry 1-2 sie nie zgadzaja: " + pesel)

    data_miesiac = data_ur.month
    if 1800 <= data_ur.year <= 1899:
        data_miesiac += 80
    if 2000 <= data_ur.year <= 2099:
        data_miesiac += 20

    if int(pesel[2:4]) != data_miesiac:
        raise ValueError("Cyfry 3-4 sie nie zgadzaja: " + pesel)
    if int(pesel[4:6]) != data_ur.day:
        raise ValueError("Cyfry 5-6 sie nie zgadzaja: " + pesel)
    if pesel_nums[9] % 2 != plec:
        raise ValueError("Cyfry porzadkowe 7-10 sie nie zgadzaja: " + pesel)
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = sum([num * waga for num, waga in zip(pesel_nums, wagi)])
    suma %= 10
    suma = 10 - suma
    suma %= 10
    if suma != pesel_nums[-1]:
        raise ValueError("Suma kontrolna sie nie zgadza: " + pesel)


def sr_wieku(mode=0):
    """
    Funkcja sprawdza poprawnosc dat i liczy srednia wieku

    :raise ValueError
    :param mode: tryb 0 - restrykcyjnym, 1 - liberalnym
    :return: srednia ilosc dni wieku
    """
    dni = []
    with open("daty.in") as pl:
        lines = [line.rsplit() for line in pl]
        for line in lines:
            if len(line) != 3:
                if mode == 0:
                    raise ValueError("Data nie jest pelna: " + str(line))
                else:
                    continue
            else:
                dzien = int(line[0])
                miesiac = int(line[0])
                rok = int(line[2])

                if miesiac < 0 or miesiac > 12:
                    if mode == 0:
                        raise ValueError("Miesiac nie jest poprawny")
                    else:
                        continue

                if ((rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0) and miesiac == 2 and dzien != 29:
                    if mode == 0:
                        raise ValueError("Data (rok przestepny) nie jest poprawna")
                    else:
                        continue

                warunki = [(1, 31), (2, 28), (3, 31), (4, 30), (5, 31), (6, 30), (7, 31), (8, 31), (9, 30), (10, 31), (11, 30), (12, 31)]
                for warunek in warunki:
                    if warunek[0] == miesiac and warunek[1] != dzien:
                        if mode == 0:
                            raise ValueError("Data nie jest poprawna (liczba dni nie zgadza sie)")
                        else:
                            break

                wczytana = datetime.date(rok, miesiac, dzien)
                dni.append((datetime.date.today() - wczytana).days)
    return sum(dni) / len(dni)
