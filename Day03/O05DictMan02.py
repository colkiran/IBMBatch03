
print("keys".center(60, "-"))
player = {'name': 'Tendulkar', 'age': 30, 'runs': 105, 'oppn': 'Aus', 'year': 1998, 'venue': 'perth'}
print(f"player :{player}")


kys = player.keys()
print(f"keys :{kys}")

print("-" * 60)
for k in player.keys():
    print(k, "=>", player[k])

print("values".center(60, "-"))

player = {'name': 'Tendulkar', 'age': 30, 'runs': 105, 'oppn': 'Aus', 'year': 1998, 'venue': 'perth'}
print(f"player :{player}")

vl = player.values()
print(f"vl :{vl}")

print("items".center(60, "-"))
# items = keys + values

emp = {
    'emp1' : {'name': 'Kevin', 'age': 32, 'desig': 'TL', 'gender': 'male', 'salary': 85000, 'loc': 'hyd'},
    'emp2' : {'name': 'Ruben', 'age': 36, 'desig': 'MGR', 'gender': 'male', 'salary': 130000, 'loc': 'del'},
    'emp3' : {'name': 'Tina', 'age': 30, 'desig': 'BDE', 'gender': 'female', 'salary': 45000, 'loc': 'che'}
}

print(f"emp :{emp}")

print("-" * 60)

print(f"emp1 :{emp['emp1']}")
print("-" * 60)
print(f"emp2 :{emp['emp2']}")
print("-" * 60)
print(F"emp3 :{emp['emp3']}")

print("-" * 60)
for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("-" * 60)

player = {'name': 'Tendulkar', 'age': 30, 'runs': 105, 'oppn': 'Aus', 'year': 1998, 'venue': 'perth'}
print(f"player :{player}")

print(f"Name :{player.get('name',  'Invalid Key please enter a valid one')}")
print(f"Runs :{player.get('run', 'Invalid Key please enter a valid one' )}")


print("setdefault".center(60, "-"))
cities= ['blr', 'che', 'mum', 'hyd', 'del']
print(f"cities :{cities}")

# convert the list into a dictionnary
res = dict.fromkeys(cities)
print(f"res :{res}")

res = dict.fromkeys(cities, 24)
print(f"res :{res}")

print("setdefault".center(60, "-"))
# setdefault will create a new key value, but never modify the existing key value

player = {'name': 'virat', 'age': 34, 'runs': 120, 'oppn': 'NZL'}
print(f"player :{player}")

player.setdefault('name', 'kholi')
player.setdefault('runs', 85)
player.setdefault('venue', 'auckland')
player.setdefault('year', 2010)

print(f"player :{player}")
