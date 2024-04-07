"""
pobierz nazwy plikow wartosci od uzytkownika
jedna to plik do skopiowania
druga to docelowa nazwa/sciezka pliku
wykonaj 'cp' na tych plikach
"""

import os

zrodlo = input("podaj plik do skopiowania")
cel = input("podaj plik docelowy")

os.system(f"cp {zrodlo} {cel}")
