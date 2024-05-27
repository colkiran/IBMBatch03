
class Animal:

    def __init__(self):
        print("Animal Contructor")
        self.age = '1 y'

    def eat(self):
        print("Animals eat.....")

class Bird(Animal):

    def __init__(self):
        super().__init__()
        self.size = '1 k'
        print("Bird Ctor......")

    def fly(self):
        print("Birds fly......")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print(cuckoo.size)
print(cuckoo.age)
print(cuckoo.__dict__)