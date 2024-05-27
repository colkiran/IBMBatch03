
from datetime import datetime


class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"Name is {self.name}\nAge is {self.age}")


    @classmethod
    def CreatePlayer(cls, fn, ln, dob):
        dob_date = datetime.strptime(dob, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
        return cls(f"{fn} {ln}", age)



fn = "Sachin"
ln = "Sharma"
dob = "1990-05-15"

ply2 = Player.CreatePlayer(fn, ln, dob)
print(ply2)

