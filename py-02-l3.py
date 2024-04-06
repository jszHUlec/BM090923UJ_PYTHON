print("""
napisz program, ktory pobiera wartosc 0-100 % od uzytkownika
Wartosc z przedzialy 0%-30% zwaraca kolor czerwony
wartosc z przedzialu 30%-80% zwaraca kolor pomaraczowy
wartosc z przedzialu 80%-100% zwraca kolor zielony
wartosc powyzej 100% wyswietla blad:
""")

soc = int(input("Podaj procent naladowania baterii: "))

if soc <= 30:
    print("Czerwony")
elif soc <= 80:
    print("Pomaranczowy")
elif soc <= 100:
    print("Zielony")
else:
    print("Bląd Poziom Czarnobyl!! Odlacz baterie!")