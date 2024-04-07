def pobierz_liczbe_int(text, komunikat_bledu):
    while True:
        try:
            x = int(input(text))
            return x
        except ValueError as e:
            print(f"{text}. {komunikat_bledu}")
            continue

def kalkulacja(p1, p2, operator):
    if operator == "+":
        return p1+p2
    elif operator == "*":
        return p1*p2
    elif operator == "/":
        return p1/p2
    elif operator == "-":
        return p1-p2
    else:
        print("error")

def pobierz_operator():
    operatory = ["+","-","/","*"]
    while True:
        operator = input("podaj operacje")
        if operator in operatory:
            return operator

print(__name__)
if __name__ == "__main__":
    print("testowa kalkulacja 2+3=5 --> ",kalkulacja(2,3,'+'))