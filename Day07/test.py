
gstname = "Sunil Gavaskar"
players = ['sachin', 'sourav', 'sehwag', 'dravid', 'yuvraj']
runs = {'odi': 21340, 'test': 15400, 't20': 2500}

def greet(gname):
    print(f'Greetings Mr.{gname}, Welcome to the event.....')

class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return f"Name is {self.name}\nAge is {self.age }"

greet("Virat Kholi")

print("-" * 60)

ply1 = Player("Dhoni", 29)
print(ply1)
