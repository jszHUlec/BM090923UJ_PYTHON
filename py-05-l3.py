
zmienna = 9

def podmien(nowa_zmienna):
    global zmienna
    zmienna = nowa_zmienna

od_uzytkownika = input("podaj wartosc: ")
podmien(od_uzytkownika)

print(zmienna)