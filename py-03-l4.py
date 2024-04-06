"""
stworz program, ktory bedzie przechowywal porty i uslugi przypisane do portu
program powinien miec menu
pozycja w menu '0' - wprowadzanie nazwy uslugi i portu
pozycja w menu '1' - wyswietlenie zawartosci slownika
pozycja w menu '2' - wyjscie z programu
"""

# stworz pusty slownik
# stworz menu, ktore bedzie wysweitlane w petli while
# jezeli uzytkownik wcisniej 1 to wyswietl zawartosc slownika

protokoly = {}
usluga = ""
port = 0

while True:
    print(""" Menu
    0) wprowadzanie nazwy uslugi oraz portu
    1) wyswietlenie zawarosci slownika
    2) wyjscie z programu
    """)

    user = input(("wybierz pozycje menu: ")).strip()
    if user == "2":
        break
    elif user == "1":

        print(protokoly)
    elif user == "0":
        usluga = input("Wprowadz nazwe uslugi np. http: ").lower().strip()
        while True:
            port = input("Wprowadz numer portu  uslugi np. http: ").lower().strip()
            if port.isdecimal():
                protokoly[usluga] = int(port)
                break
            elif port == "menu":
                break
            else:
                print("Oszalales! Port jest liczbą! Sprubuj ponownie! lub napisz menu aby poworocic do menu")

    else:
        print("Bledny wybor")

print("Koniec programu")