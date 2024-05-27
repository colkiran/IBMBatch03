
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C++', 'JAVA', 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'ReactJS']

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def __len__(self):
        # return len(self.tech)
        return len(self.name)

    def __iter__(self):
        return iter(self.tech)


emp1 = Employee("Louis", 45000)
print(emp1)

print("-" * 60)
print(len(emp1))

print("-" * 60)
print([emp for emp in emp1])        # list comprehension