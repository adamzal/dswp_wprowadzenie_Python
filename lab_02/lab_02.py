# Zadanie 1
text = input("Wprowadź tekst: ")
sep_1 = input("Wprowadź separator źródłowy: ")
sep_2 = input("Wprowadź separator docelowy: ")
print(sep_2.join(text.split(sep_1)))
print(text.replace(sep_1, sep_2))

# Zadanie 2
var = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz " \
      "pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później " \
      "zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach "\
      "60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym " \
      "różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, " \
      "jak Aldus PageMaker "

# Zadanie 3
litera_1 = "a"
litera_2 = "e"
liczba_liter1 = var.count(litera_1)
liczba_liter2 = var.count(litera_2)
print(f"W tekście jest {liczba_liter1} liter {litera_1} oraz {liczba_liter2} liter {litera_2}")
