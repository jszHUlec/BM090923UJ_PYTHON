class Server:
    def __init__(self, color, window_number, price):
        self.color = color
        self.window_number = window_number
        self.price = price

    def wysweitl(self):
        print(self.color,self.window_number, self.price)

car1 = Car("blue",4,300)
car2 = Car("red",2,600)

moje_samochody = [car1, car2]

for samochod in moje_samochody:
    samochod.wysweitl()


