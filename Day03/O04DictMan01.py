
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)
d2 = {'name': 'Sachin', 'age': 32, 'runs': 85, 'oppn': 'Aus'}
print(f'd2: {d2}')
print(type(d2))

print("-" * 60)
d3 = dict([('name', 'rahul'), ('age', 29), ('runs', 102), ('oppn', 'SA')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict(name="sehwag", age=30, runs=150, oppn='NZL')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
# CRUD
# create
player = {'name': 'Sachin', 'age': 30, 'runs': 90, 'oppn': 'Aus'}
print(f"Player :{player}")

print("-" * 60)
# read
print(f"Name :{player['name']}")
print(f"Age  :{player['age']}")

print("-" * 60)
# iterate through the dictionary
for i in player:
    print(i, "=>", player[i])

print("-" * 60)
# update - modify and add new key and value
print(f"player :{player}")

player['name'] = "Tendulkar"
player['runs'] = 105
player['year'] = 1998
player['venue'] = 'perth'

print(f"player :{player}")

print("-" * 60)
# delete
del player['age']
del player['year']

print(f"player :{player}")

print("-" * 60)
print(dir(player))
