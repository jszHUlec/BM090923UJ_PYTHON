"""
wprowadz dane od uzytkownika i zaszyfruj jest w base64.
Zapisz to do pliku i odczytaj plik jako zwykly tekst
"""

import base64

print("Podaj teskt, a ja go zapisze do pliku.\nEXIT konczy wprowadzanie tesktu")
with open("base64.txt","w+") as file:
    while True:
        text = input(": ")
        if text.strip().upper() == "EXIT":
            break
        encoded = base64.b64encode(text.encode("UTF-8"))
        file.write(encoded.decode("UTF-8"))
        file.write("\n")

    file.seek(0)
    for linijka in file.readlines():
        decoded = base64.b64decode(linijka)
        print(linijka, " : ",decoded)


