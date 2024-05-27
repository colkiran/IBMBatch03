
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        print("getter called....")
        return self.__price

    def set_price(self, prc):
        print("setter called.....")
        self.__price = prc

    def del_price(self):
        print("deleter called......")
        self.__price = 0

    price = property(get_price, set_price, del_price)

coke = Product(35)
print(coke.price)
coke.price = 85
print(coke.price)
del coke.price
print(coke.price)
