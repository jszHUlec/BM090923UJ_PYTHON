"""
Napisz program, ktory pobiera nazwe pliku i wyswietla go linijka po linijce w konsoli
"""

plik_do_otwarcia = input("podaj sciezke")

with open(plik_do_otwarcia, "r") as file:
    for linijka in file.readlines():
        print(linijka, end="")