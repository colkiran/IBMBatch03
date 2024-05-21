
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4.3, 5.0, 6.5, 7+2j, 8-3j, 'nine', 'ten', 'eleven', True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
# CRUD

l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

# indexing
print(f"l1[0] :{l1[0]}")
print(f"l1[4] :{l1[4]}")

# iterate
for i in l1:
    print(i, end=" ")
print()

print("-" * 60)
# updation

print(f"l1 :{l1}")
l1[2] = 300
print(f"l1 :{l1}")

# insert a new value
l1[1] = 150
print(f"l1 :{l1}")

# l1[5] = 10
# print(f"l1 :{l1}")

print("-" * 60)
# delete element
print(f"l1 :{l1}")
del l1[2]
del l1[3]
print(f"l1 :{l1}")


print("-" * 60)
# print(dir(l1))
