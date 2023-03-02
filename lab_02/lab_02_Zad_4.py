text = "Adam Zalewski"
index = 155461
dicti = {"Adam": len(text.split(" ")[0]), "Zalewski": len(text.split(" ")[1])}


class Osoba:
    imie = "Adam"
    nazwisko = "Zalewski"
    index = 155461

    def __format__(self, f):
        return f[4:10]


print('\n{:>20}'.format(text), index)
print('{:20}'.format(text), index)
print('{:^20}'.format(text), index)
print('{:.10}'.format(text), index, "\n")

print('{:f}'.format(index), text)
print('{:10d}'.format(index), text)
print('{:010d}'.format(index), text, "\n")

print('{Adam} {Zalewski}'.format(**dicti))

print('\n{o.imie} + {o.nazwisko} = {o.index}'.format(o=Osoba()), "\n")

print('{:Adam Zalewski 155461}'.format(Osoba()))
