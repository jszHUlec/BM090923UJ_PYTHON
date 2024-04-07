"""
Napisz program, ktory pobiera od uzytkownika linijki tekstu
ktore musza byc zapisane do pliku
Po wpisaniu exit konczymy wprowadzanie danych i zamykamy plik
"""

print("Podaj teskt, a ja go zapisze do pliku.\nEXIT konczy wprowadzanie tesktu")
i = 0
with open("pl-04-l3.txt","w") as file:
    while True:
        i = i+1
        text = input(str(i)+": ")
        if text.strip().upper() == "EXIT":
            break
        file.write(text+"\n")
