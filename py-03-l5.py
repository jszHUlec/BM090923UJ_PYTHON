"""
mamy do dysozycji budzet i owoce w sklepie
napisz program, ktory dodaje do koszyka produkty
jezeli mamy na nie pieniadze.
wpisanie 'exit' konczy program i podsumowuje koszyk
"""
budzet = 20
owoce = {"jablka":5, "mandarynki":10, "pomarancza":8, "wisnia":15}
koszyk = []

print("""
    wpisz owoc, zeby dodac do koszyka. 
    Wpisanie 'exit' konczy program i podsumowuje koszyk
    Wpisanie 'podglad' wyswietla bierzacy stan koszyka
""")
while True:
    print(owoce)
    wybor = input("co chcesz kupic ?").lower().strip()
    if wybor == 'exit':
        print(budzet, koszyk)
        break
    elif wybor == 'podglad':
        print(budzet, koszyk)
    elif wybor in owoce:
        if budzet - owoce[wybor] < 0:
            print("nie masz srodkow na ten zakup")
            continue
        budzet = budzet - owoce[wybor]
        koszyk.append(wybor)
    else:
        print("bledna komenda")

print("Koniec programu")



