
class Animal:

    def __init__(self):
        print("Animal Ctor......")
        self.a = 10

    def eat(self):
        print("Animals eat.....")

    def fun(self):
        print("Animal class fun method......")

class Person:

    def __init__(self):
        print("Person ctor.....")
        self.b = 20

    def talk(self):
        print("Person talks.....")

    def fun(self):
        print("Person class fun method......")

class Girl(Animal, Person):

    def __init__(self):
        super().__init__()
        Person.__init__(self)
        print("Girl Ctor......")
        self.g = 30

    def walk(self):
        print(f"Girls walk.......")

gracy = Girl()
gracy.eat()
gracy.talk()
gracy.walk()

gracy.fun()

print(gracy.__dict__)

