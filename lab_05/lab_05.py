import numpy as np
import math
import random


# Zadanie 1
n = 10
A = {1 / x for x in range(1, 11)}
B = {2 * x for x in range(1, n + 1)}
C = {x for x in range(1, n + 1) if x % 4 == 0}
print(A)
print(B)
print(C)

# Zadanie 2
M = np.random.rand(4, 4)
li = [M[i, i] for i in range(len(M))]
print(M)
print(li)

# Zadanie 3
text = input("Wpisz tekst: ")
split = text.split()
wynik = [(i, [ord(a) for a in i]) for i in split]
print(wynik)

# Zadanie 4


def row_kwadratowe(a: int | float, b: int | float, c: int | float):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        # brak pierwiastków
        return -1
    elif delta == 0:
        # jeden pierwiastek
        x = (-b) / (2 * a)
        return x
    else:
        # równanie ma dwa pierwiastki
        x1 = (- b - math.sqrt(delta)) / (2 * a)
        x2 = (- b + math.sqrt(delta)) / (2 * a)
        return x1, x2


print(row_kwadratowe(6, 1, 3))
print(row_kwadratowe(1, 2, 1))
print(row_kwadratowe(1, 4, 1))

# Zadanie 5


def rzut_kostka(_n):
    o = [i-i for i in range(6)]
    for i in range(_n):
        r = random.randint(0, 5)
        o[r] += 1
    w = [(f'oczka {i}', f'rzutów {o[i - 1]}') for i in range(1, 7)]
    return w


print(rzut_kostka(1000))


# Zadanie 6
def abc(*tekst: str):
    if len(tekst) == 0:
        return []
    else:
        return sorted(tekst)


print(abc("Ala", "ma", "kota"))


# Zadanie 7
def punkty(**var):
    suma = 0
    for d in var:
        if type(var[d]) == list:
            for i in var[d]:
                suma += i
        else:
            suma += var[d]
    return suma


print(punkty(a=[65, 134], b=25, c=27))
