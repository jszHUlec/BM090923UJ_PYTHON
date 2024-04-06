"""
pobierz od uzytkownika liczbe wierszy
Pobierz od uzytkowniak liczbe kolumn
"""
# pobierz liczbe wierszy
# pobierz liczbe kolumn

# stworz w peli tablice dwu wymiarowa
# z wartosciami numerycznymi reprezentujacymi wiersz/kolumna

liczba_wierszy = int(input("podaj liczbe wierszy: "))
liczba_kolumn = int(input("podaj liczbe kolumn: "))
tablica = list()

for i in range(liczba_wierszy): # wiersze
    wiersz = list()
    for j in range(liczba_kolumn): # kolumny
        wiersz.append(i + j)
    tablica.append(wiersz)

print(tablica)
