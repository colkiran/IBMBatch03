"""
sort    - will sort the original list
sorted  - takes a copy of the list sorts it and returns it
"""
print("sort".center(60, "-"))

l1 = [9, 4, 1, 10, 6, 8, 2, 5, 7, 3]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"ascending :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"descending :{res_desc}")

print("-" * 60)
l1 = [9, 'zebra', 'apple', 4, 'gree', 'blue', 1, 'orange', 'white', 10, 6, 'pink', 'violet',  8,  'cat', 'dog', 2, 'elephant', 'tiger', 5, 7, 3, 190, 1654, 28, 207, 2138]
print("-" * 60)
print(f"l1 :{l1}")
res = sorted(l1, key=ascii)

print("-" * 60)
print(f"res :{res}")

idx = 0
for i in range(0, len(res)):
    if type(res[i]) == int:
        idx = i
        break
print(f"index :{idx} => {res[idx]}")
print("-" * 60)
print(res[:idx] + sorted(res[idx:]))

print("-" * 60)
cities = {'vishakapatnam', 'delhi', 'bangalore', 'chennai', 'thiruvananthapuram', 'ooty', 'hyderabad', 'pune', 'mumbai', 'kolkotta'}
print(f"cities :{cities}")

# sort the cities based on the no of characters in each city

res = sorted(cities, key=len)
print(f"res :{res}")

print("reversed".center(60, "-"))
l1 =[1, 2, 3, 4, 5]
print(f"l1 :{l1}")

res = list(reversed(l1))
print(f"res :{res}")
