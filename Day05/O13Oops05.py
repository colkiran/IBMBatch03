
class Player:

    def __init__(self, name, age):          # constructor
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 34)
ply1.get_details()

print("-" * 60)
ply2 = Player("Rahul", 31)
ply2.get_details()

ply2.runs = 150

print("-" * 60)

print(ply1.__dict__)
print(ply2.__dict__)
