
class Animal:

    def eat(self):
        print("Animals eat.....")

class Bird(Animal):

    def fly(self):
        print("Birds fly.....")

class Chicken(Bird):

    def Msg(self):
        print("Chikens are breededfor consumption....")
        
    def fly(self):
        print(f"Chickens seldom fly......")


chic = Chicken()
chic.eat()
chic.fly()
chic.Msg()
