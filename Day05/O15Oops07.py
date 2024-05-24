
class Player:
    def __init__(self, name, age):          # constructor
        self.name = name
        self.age = age
        print("Player Ctor......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def CreatePlayer(cls, fn, ln, age):
        print("factory.....")
        return cls(f"{fn} {ln}", age)       # calls constructor


ply1 = Player("Sachin", 32)
ply1.get_details()

print("-" * 60)

# player2 name is in fn and ln
ply2 = Player.CreatePlayer("Virat", "Kholi", 27)
ply2.get_details()



