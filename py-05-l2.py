"""
napisz kilka funkcji zwracajacych rozne typy danych
i sprawdz jakego typu dane sa zwracane
"""
x1 = "jeden"
x2 = "dwa"
def return_list(x1, x2):
    return [x1,x2]
def return_tupla(x1, x2):
    return (x1,x2)
def return_slownik(x1, x2):
    return {x1:x2}
def return_int():
    return 23
def return_bool():
    return True

print( type( return_list(x1,x2) ) ) # [x1,x2]
print( type( return_tupla(x1,x2) ) ) # [x1,x2]
print( type( return_slownik(x1,x2) ) ) # [x1,x2]
print( type( return_int() ) ) # [x1,x2]
print( type( return_bool() ) ) # [x1,x2]
