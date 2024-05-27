
class Employee:

    def __init__(self, name):
        self.__name = name              # private Variable
        self.tech = ['C++', 'JAVA', 'J2EE', 'Spring', 'Hibernate', 'AngularJS', 'ReactJS']

    def __str__(self):
        return self.__name + ' - ' + ", ".join([str(v) for v in self.tech])


emp1 = Employee("Ben")
print(emp1)

print("-" * 60)
# print(emp1.__dict__)
emp1._Employee__name = 'Johnson'
print(emp1)

print("-" * 60)
print(emp1.__dict__)
