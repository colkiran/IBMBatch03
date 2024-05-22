
print("pop".center(60, "-"))
player = {'name': 'virat', 'age': 34, 'runs': 120, 'oppn': 'NZL', 'venue': 'auckland', 'year': 2010}

res = player.pop('oppn')
print(f"res :{res}")

res = player.pop('runs')
print(f"res :{res}")

print(f"player :{player}")

print("popitem".center(60, "-"))
player = {'name': 'virat', 'age': 34, 'runs': 120, 'oppn': 'NZL', 'venue': 'auckland', 'year': 2010}
print(f"player :{player}")

res = player.popitem()
print(f"res: {res}")

res = player.popitem()
print(f"res :{res}")

print(f"player :{player}")

print("update".center(60, "-"))
emp1 = {'name': 'Kevin', 'age': 32, 'desig': 'TL', 'gender': 'male', 'salary': 85000}

emp2 = {'name': 'Ruben', 'age': 36, 'desig': 'MGR', 'gender': 'male',  'loc': 'del'}

print(f"emp1 :{emp1}")

print("-" * 60)

print(f"emp2 :{emp2}")

emp1.update(emp2)

print(f"emp1 :{emp1}")

print("clear".center(60,"-"))
emp1 = {'name': 'Kevin', 'age': 32, 'desig': 'TL', 'gender': 'male', 'salary': 85000}

print(f"emp1 :{emp1}")
emp1.clear()

print(f"emp1 :{emp1}")

print("copy".center(60, "-"))
emp1 = {'name': 'Kevin', 'age': 32, 'desig': 'TL', 'gender': 'male', 'salary': 85000}
print(f"emp1 before :{emp1}")

# copy emp1 into emp2
emp2 = emp1         # shallow copy
print(f"emp2 before :{emp2}")

emp2['loc'] = 'del'
emp2['dept'] = 'finance'

print(f"emp2 after :{emp2}")
print(f"emp1 after :{emp1}")

# complete this code as assignment