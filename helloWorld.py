x = 1
while True: # for x in range(4):
    try:
        wybor = int(input("podaj cyfre a ja ci podam jej potege").lower().strip())
        print("potega:",wybor * wybor)
        break
    except ValueError as blad:
        print("podales litere zamiast cyfry!!!!", blad)
        print("to byla twoja ", x , "proba")
        x = x + 1
    else:
        print("wykonywany gdy bez bledu")
    finally:
        print("wykonywany zawsze")

print("koniec programu")