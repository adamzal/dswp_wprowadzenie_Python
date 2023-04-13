from typing import Any

# Zadanie 1
def extract_numbers(vals: list[Any]) -> list[int | float]:
    return list(filter(lambda x: isinstance(x, (int, float)), vals))

# Zadanie 2
tekst = input("Podaj wyrazy: ").split()
tekst_sort = sorted(tekst, key=lambda x: len(x), reverse=True)
print(tekst_sort)

# Zadanie 3
from typing import List, Union

def zad3(lst: List[Union[int, str]], reverse: bool = False) -> List[Union[int, str]]:
    int_lst = sorted([x for x in lst if isinstance(x, int)], reverse=reverse)
    str_lst = sorted([x for x in lst if isinstance(x, str)], reverse=reverse)
    if reverse:
        return str_lst + int_lst
    else:
        return int_lst + str_lst

# Zadanie 4
import csv
import datetime
import os

if os.path.exists("new_zamowienia.csv"):
    os.remove("new_zamowienia.csv")
if os.path.exists("zamowienia_polska.csv"):
    os.remove("zamowienia_polska.csv")
if os.path.exists("zamowienia_niemcy.csv"):
    os.remove("zamowienia_niemcy.csv")

with open("zamowienia.csv", encoding='utf-8', newline="") as file:
    with open("new_zamowienia.csv", "a", encoding='utf-8', newline="") as new_file:
        with open("zamowienia_polska.csv","a",encoding='utf-8', newline="") as poland_file:
            with open("zamowienia_niemcy.csv","a",encoding='utf-8', newline="") as german_file:

                reader = csv.DictReader(file, delimiter=';')
                writer_new = csv.DictWriter(new_file, fieldnames=reader.fieldnames, delimiter=";")
                writer_poland = csv.DictWriter(poland_file, fieldnames=reader.fieldnames, delimiter=";")
                writer_german = csv.DictWriter(german_file, fieldnames=reader.fieldnames, delimiter=";")

                writer_new.writeheader()
                writer_poland.writeheader()
                writer_german.writeheader()

                utarg_replace = lambda wiersz: dict(wiersz,
                                                    Utarg=wiersz['Utarg'].replace(" z�", "").replace(",", ".").replace(
                                                        " ", ""))
                data_replace = lambda wiersz: dict(wiersz, **{
                    'Data zamowienia': datetime.datetime.strptime(wiersz["Data zamowienia"], "%d.%m.%Y").strftime(
                        "%Y-%m-%d")})

                for wiersz in map(data_replace, map(utarg_replace, reader)):
                    writer_new.writerow(wiersz)
                    if wiersz["Kraj"] == "Polska":
                        writer_poland.writerow(wiersz)
                    if wiersz["Kraj"] == "Niemcy":
                        writer_german.writerow(wiersz)


# Zadanie 5
def zad5(d, f):
    return {i: sorted(filter(lambda x: isinstance(x, int), j), key=f) for i, j in d.items()}
