a = input("Podaj linię danych:\n")
b = input("Podaj separator źródłowy:\n")
c = input("Jak chcesz podzielić wyrazy:\n")

d = a.split(b)
e = c.join(d)
print(d)
print(e)

lorem = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz " \
        "pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później " \
        "zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w " \
        "latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z " \
        "zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach " \
        "osobistych, jak Aldus PageMaker"

myName = "Bartek"
mySurname = "Wojciechowski"
litera_1 = myName[2]
litera_2 = mySurname[3]

print(f"W tekście jest {lorem.count(litera_1)} liter {litera_1} oraz {lorem.count(mySurname)} liter {litera_2}")
