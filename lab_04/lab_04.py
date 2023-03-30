import sys
import this
import string
import random

# Zadanie 1
a = int(input("Wprowadź liczbę: "))
print(bin(a), oct(a), hex(a))

# Zadanie 2
i = input("Wprowadź dane: ")
try:
    print(f"Wartość po rzutowaniu na int to: {int(i)}")
except Exception as e:
    print(f"{i} nie można zrzutować na int.", e)

try:
    print(f"Wartość po rzutowaniu na float to: {float(i)}")
except Exception as e:
    print(f"{i} nie można zrzutować na float.", e)

# Zadanie 3
print("Wprowadź liczbę: ", end="")
d = sys.stdin.readline()
s = ""
for i in range(len(d) - 1):
    if i != len(d) - 2:
        s += f"{10 ** (len(d) - i - 2)}*{d[i]} + "
    else:
        s += f"{10 ** (len(d) - i - 2)}*{d[i]}"
sys.stdout.write(f"Liczbę można zapisać jako: {s}")

# Zadanie 4
t = input("Wprowadź tekst: ")
s = ""
for i in t:
    if i not in string.ascii_letters:
        s += i
    else:
        s += this.d.get(i)
print(s)

# Zadanie 5
t = input("Wprowadź tekst: ")
t = t.split(" ")
t.sort(key=len)
print(t)

# Zadanie 6
s = [
    "Koleżanki i koledzy	realizacja nakreślonych zadań programowych	zmusza nas do przeanalizowania	istniejących "
    "warunków administracyjno-finansowych.",
    "Z drugiej strony	zakres i miejsce szkolenia kadr	spełnia istotną rolę w kształtowaniu	dalszych kierunków rozwoju.",
    "Podobnie	stały wzrost ilości i zakres naszej aktywności	wymaga sprecyzowania i określenia	systemu "
    "powszechnego uczestnictwa.",
    "Nie zapominajmy jednak, że	aktualna struktura organizacji	pomaga w przygotowaniu i realizacji	postaw uczestników "
    "wobec zadań stawianych przez organizację.",
    "W ten oto sposób	nowy model działalności organizacyjnej	zabezpiecza udział szerokiej grupie w kształtowaniu	"
    "nowych propozycji.",
    "Praktyka dnia codziennego dowodzi, że	dalszy rozwój różnych form działalności	spełnia ważne zadania w "
    "wypracowaniu	kierunków postępowego wychowania.",
    "Wagi i znaczenia tych problemów nie trzeba szerzej uzasadniać, ponieważ	stałe zabezpieczenie informacyjno "
    "programowe naszej działalności	umożliwia w większym stopniu tworzenie	systemu szkolenia kadry odpowiadającego "
    "potrzebom.",
    "Różnorakie i bogate doświadczenia	wzmacnianie i rozwijanie struktur	powoduje docenianie wagi	odpowiednich "
    "waruknków aktywizacji.",
    "Troska organizacji, a szczególnie	konsultacja z szerokim aktywem	przedstawia intersującą próbę sprawdzenia	"
    "modelu rozwoju.",
    "Wyższe założenia ideowe, a także	rozpoczęcie powszechnej akcji kształtowania postaw	pociąga za sobą proces "
    "wdrażania i unowocześniania	form oddziaływania."]
w = []
for i in s:
    w += [i.split("\t")]

n = int(input("Wpisz ilość zdań: "))
for i in range(n):
    a = random.randint(0, len(w) - 1)
    b = random.randint(0, len(w) - 1)
    c = random.randint(0, len(w) - 1)
    d = random.randint(0, len(w) - 1)
    print(w[a][0], w[b][1], w[c][2], w[d][3])
