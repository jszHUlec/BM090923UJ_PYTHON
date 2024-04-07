"""
poprosz uzytkownika o podanie 2 wartosci
podziel obie wartosci przez siebie
upewnij sie, ze druga liczba nie jest 0
"4 / 2 = 2 , 2 / 0 = 'blad' "
Gdy mamy 'blad' popros uzytkownika o podanie nowych wartosci!
"""
class BlednaOperacjaError(Exception):
    pass

operacje = ['+','-','*','/']
while True:
    try:
        x = int(input("Podaj pierwsza wartosc: ").strip())
        y = int(input("Podaj druga wartosc: ").strip())
        operacja = input("podaj operacje +,-,/,*: ")
        if operacja in operacje:
            if operacja == operacje[0]:
                print("x + y =", x+y)
            elif operacja == operacje[1]:
                print("x - y =", x - y)
            elif operacja == operacje[2]:
                print("x * y =", x * y)
            elif operacja == operacje[3]:
                print("x / y =", x / y)
        else:
            raise BlednaOperacjaError

        # print("Rezultat x/y = ", x / y)
        break

    except ValueError:
        print("Podaj tylko liczby!")
    except ZeroDivisionError:
        print("Nie dziel przez zero! Sprobuj jeszcze raz!")
    except BlednaOperacjaError:
        print("Zla operacja! Sprobuj jeszcze raz!")
    except Exception:
        print("ogolny blad w aplikacji/n")


        # enter w Win to jest /r/n

