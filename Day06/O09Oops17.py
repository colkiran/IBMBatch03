
class Animal:

    def __init__(self):
        print("Animal Ctor......")
        self.age = 1

    def eat(self):
        print("All animals eat.....")

class Bird(Animal):
    def fly(self):
        print("birds fly....")

class Fish(Animal):

    def swim(self):
        print('fishes swim....')

cuckoo = Bird()
cuckoo.fly()
cuckoo.eat()
print("-" * 60)
dolphin = Fish()
dolphin.swim()
dolphin.eat()

print("-" * 60)
print(cuckoo.__dict__)
print(dolphin.__dict__)

print("-" * 60)
print(isinstance(cuckoo, Bird))
print(isinstance(cuckoo, Animal))
print(isinstance(dolphin, Animal))
print(isinstance(dolphin, Animal))
print(isinstance(cuckoo, Animal))

print(isinstance(dolphin, object))
print("-" * 60)

print(issubclass(Bird, Animal))
print(issubclass(Fish, Animal))
print(issubclass(Bird, Animal))



