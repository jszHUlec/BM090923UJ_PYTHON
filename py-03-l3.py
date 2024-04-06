koniec_gry = 0

while True: #True / False
    x = input("wprowadz liczbe: ").lower().strip()
    if x.isdecimal():
        x = int(x)
    elif x == "exit":
        koniec_gry = 1
        break
    else:
        print("Blad: a komenda badz liczba")

    if x == 35:
        break
    else:
        print("Chybiles! Sprobuj jeszce raz")

if koniec_gry == 0:
    print("Hurra wygrales")
else:
    print("koniec programu")