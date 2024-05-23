
emp1 = {'name': 'Kevin', 'age': 32, 'desig': 'TL', 'gender': 'male', 'salary': 85000}

print(f"emp1 before :{emp1}")
print("-" * 60)
emp2 = emp1         # shallow copy
print(f"emp2 before :{emp2}")

emp2['loc'] = 'del'
emp2['dept'] = 'finance'

print("-" * 60)
print(f"emp2 after :{emp2}")
print(f"emp1 after :{emp1}")

print("=" * 60)
emp3 = {'name': 'Kevin', 'age': 32, 'desig': 'TL', 'gender': 'male', 'salary': 85000}
print(f"emp3 before :{emp3}")

# copy emp3 into emp4
emp4 = emp3.copy()      # deep copy
print(f"emp4 before :{emp4}")

print("-" * 60)

emp4['loc'] = 'del'
emp4['dept'] = 'finance'

print(f"emp4 after :{emp4}")
print(f"emp3 after :{emp3}")

print("=" * 60)
emp5 = {'name': 'Kevin', 'age': 32, 'desig': 'TL', 'gender': 'male', 'salary': {'hp': 25000,  'TCS': 35000}}
print(f"emp5 before :{emp5}")

# copy emp5 into emp6
emp6 = emp5.copy()      # deep copy
print(f"emp6 before :{emp6}")

emp6['salary']['seimens'] = 45000
emp6['salary']['hcl'] = 60000

print(f"emp6 after :{emp6}")
print(f"emp5 after :{emp5}")

print("=" * 60)
from copy import deepcopy

emp7 = {'name': 'Kevin', 'age': 32, 'desig': 'TL', 'gender': 'male', 'salary': {'hp': 25000,  'TCS': 35000}}
print(f"emp7 before :{emp7}")

# copy emp7 into emp8
emp8 = deepcopy(emp7)           # deep copy
print(f"emp8 before :{emp8}")

emp8['salary']['seimens'] = 45000
emp8['salary']['hcl'] = 60000

print(f"emp8 after :{emp4}")
print(f"emp7 after :{emp3}")
