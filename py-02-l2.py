print("""
Pobierz od uzytkownika jego wiek i imie
jezeli jest osoba pelnoletnia,
to przed imieniem wysweitl Pan/Pani
jezeli jest niepelnoletni to wyswietl "czesc mlody/mloda" (bez imienia)
""")

age = int(input("Podaj swoj wiek: "))
name = input("Podaj imie: ")



if age >= 18 and age < 50:
        print("Cześć Pan/Pani " + name + " !")
elif age >= 50:
    print("Witam Panie starszy "+name+" !")
else:
    print("Cześć Mlody/a " + name + " !")

