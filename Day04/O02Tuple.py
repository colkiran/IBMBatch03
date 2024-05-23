
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 60)
t2 = (1, 2, 3, 4.1, 5.2, 6.9, 7 + 2j, 8 - 1j, 'nine', 'ten', True, False)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 60)
t3 = tuple([1, 2, 3, 4, 5])
print(f"t3 :{t3}")
print(type(t3))

print("-" * 60)
t4 = 1,
print(f"t4 :{t4}")
print(type(t4))

print("-" * 60)
t5 = 1, 2, 3, 4, 5
print(f"t5 :{t5}")
print(type(t5))

print("-" * 60)
# TUPLES ARE IMMUTABLE  - its an immutable list

# t1 = (1, 2, 3, 4, 5)
# print(f"t1 :{t1}")
# t1[2] = 300

print(dir(t1))
