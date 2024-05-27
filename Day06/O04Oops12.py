"""
immutable object - not have setter method
__setitem__ , __getitem__
"""

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C++', 'JAVA', 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'ReactJS']

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __iter__(self):
        return iter(self.tech)

    def __len__(self):
        return len(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, indx):
        return self.tech[indx]

    def __setitem__(self, indx, val):
        self.tech[indx] = val


emp1 = Employee("Peter", 65000)
print(emp1)
print("-" * 60)

print([emp for emp in emp1])
print("-" * 60)

print(len(emp1))
print("-" * 60)

emp1.append("Python")
print([emp for emp in emp1])
print("-" * 60)

x = emp1[3]
print(f"x :{x}")
print("-" * 60)

emp1[4] = "Docker"
print([emp for emp in emp1])


