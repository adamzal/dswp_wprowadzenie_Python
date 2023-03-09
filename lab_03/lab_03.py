# Zadanie 1
import string

l_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l_2 = list()

for i in range(int(len(l_1) // 2)):
    l_2 += [l_1.pop()]

l_2.sort()
print(l_1, l_2)

# Zadanie 2
l_1.extend(l_2)
print(l_1)

# Zadanie 3
tekst = input("Wpisz teskt: ")
tekst = tekst.lower()
tab=list()
for i in tekst:
    if i not in tab and i in string.ascii_lowercase:
        tab+=[i]
tab.sort()
print(tab)

# Zadanie 4
rok = {1: "Styczeń", 2: "Luty", 3: "Marzec", 4: "Kwiecień", 5: "Maj", 6: "Czerwiec", 7: "Lipiec", 8: "Sierpień",
       9: "Wrzesień", 10: "Październik", 11: "Listopad", 12: "Grudzień"}

# Zadanie 5
year = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"}
months = {'pl': rok, 'en': year}
print(months['pl'][4])

# Zadanie 6
tekst = "Marianna"
tab = [i for i in tekst]
wynik = dict.fromkeys(tab, 1)
print(wynik)

# Zadanie 7
tekst = input("Wpisz teskt: ")
tekst = tekst.lower()
tab_ascii = [[i, 0, ""] for i in string.ascii_lowercase]
tab_digits = [[i, 0, ""] for i in string.digits]

sum_ascii = 0
for i in tekst:
    if i in string.ascii_lowercase:
        tab_ascii[string.ascii_lowercase.index(i)][1] += 1
        sum_ascii += 1

sum_digits = 0
for i in tekst:
    if i in string.digits:
        tab_digits[string.digits.index(i)][1] += 1
        sum_digits += 1

if sum_ascii > 0:
    for i in tab_ascii:
        i[2] = "{:.2f}%".format(i[1] / sum_ascii * 100)

if sum_digits > 0:
    for i in tab_digits:
        i[2] = "{:.2f}%".format(i[1] / sum_digits * 100)

print(tab_ascii)
print(tab_digits)
