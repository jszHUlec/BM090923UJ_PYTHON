# define Python user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass

# you need to guess this number
number = 18

try:
    input_num = int(input("Podaj swoj wiek: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("mozesz glosowac")

except Exception as e:
    print("blad: Musisz byc osoba pelnoletnia")