
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __add__(self, other):
        return Employee("noname", self.salary + other.salary)

    def __sub__(self, other):
        return Employee("noname", self.salary - other.salary)

    def __mul__(self, other):
        return Employee("noname", self.salary * other.salary)

    def __truediv__(self, other):
        return Employee("noname", self.salary / other.salary)

    def __floordiv__(self, other):
        return Employee("noname", self.salary // other.salary)


emp1 = Employee("John", 15000)
print(emp1)

print("-" * 60)
emp2 = Employee("Michael", 10000)
print(emp2)

print("-" * 60)
# print(f"add :{emp1 + emp2}")
emp3 = emp1 + emp2
print(emp3)


print("-" * 60)
# print(f"sub :{emp1 - emp2}")
emp4 = emp1 - emp2
print(emp4)


print("-" * 60)
# print(f"Mul :{emp1 * emp2}")
emp5 = emp1 * emp2
print(emp5)

print("-" * 60)
# print(f"Div :{emp1 / emp2}")
emp6 = emp1 / emp2
print(emp6)

print("-" * 60)
# print(f"Div :{emp1 // emp2}")
emp7 = emp1 // emp2
print(emp7)


print("-" * 60)
e1 = Employee("a", 10)
e2 = Employee("b", 20)
e3 = Employee("c", 30)

e4 = e1 + e2 + e3 + e1 + e2 + e3
print(e4)
