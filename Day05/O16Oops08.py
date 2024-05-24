
class Player:

    def __init__(self, name, age):          # constructor
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name is {self.name}\nAge is {self.age}"

ply1 = Player("Rohit", 29)
# ply1.get_details()

print(str(ply1))
print("-" * 60)

print(ply1)         # implicitly call __str__ method

