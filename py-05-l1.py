import moja_biblioteka as mb

x1 = mb.pobierz_liczbe_int("podaj x1", "sprobuj ponownie")
x2 = mb.pobierz_liczbe_int("podaj x2", "oszalales ? podaj liczbe")
op = mb.pobierz_operator()

print(mb.kalkulacja(x1,x2,op))
