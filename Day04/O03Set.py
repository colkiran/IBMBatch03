
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 60)
s2 = {1, 2, 3, 4, 5.1, 6.4, 7.9, 8.2, 9 + 3j, 10 - 1j, True, False, 'thirteen', 'fourteen', 'fifteen', 'sixteen'}

print(f"s2 :{s2}")
print(type(s2))

print("-" * 60)
s3 = set(range(1, 11))
print(f"s3 :{s3}")
print(type(s3))

print("-" * 60)
# CRUD
s1 = {1, 2, 3, 4, 5}
print(f"s1 :{s1}")

print("-" * 60)
# read
print(f"s1 :{s1}")

print("-" * 60)
# iterate s1
for i in s1:
    print(i, end=" ")
print()

print("-" * 60)
# delete and update is not possible as it cannot be indexed
s1  = {1, 2}
# add, update, pop, remove and discard

s1.add(2)
s1.add(3)
s1.add(2)
s1.add(4)
s1.add(3)
s1.add(5)

print(F"s1 :{s1}")
# update
s1.update([1, 2, 3])
s1.update([4, 5, 6])
s1.update([2, 3, 4])
s1.update([7, 8, 9])
s1.update([1, 2, 10])

print(f"s1 :{s1}")

print("-" * 60)
# pop
res = s1.pop()
print(f"res :{res}")

res = s1.pop()
print(f"res :{res}")

print(f"s1 :{s1}")
print("-" * 60)
# remove

s1.remove(8)
s1.remove(4)

# s1.remove(1)
print(f"s1 :{s1}")
print("-" * 60)
# discard

s1.discard(2)
s1.discard(6)

s1.discard(1)
print(f"s1 :{s1}")

print("-" * 60)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("-" * 60)
print(f"A union B :{A | B}")
print(F"B union A :{B.union(A)}")

print("-" * 60)
print(f"A intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")

print("-" * 60)
print(f"A difference B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print("-" * 60)
print(f"A symmetricdifference B :{A ^ B}")
print(f"B symmetric difference A :{B.symmetric_difference(A)}")

# frozenset - immutable
fset = frozenset([1, 2, 3, 4, 5])
print(f"fset :{fset}")
print(type(fset))

