
print("copy".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

# copy l1 to l2
l2 = l1        # shallow copy - copy the data and the address of the list
print(f"l2 before :{l2}")

l2.append(6)
l2.append(7)
l2.append(8)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 60)
# copy function
l3 = [6, 7, 8, 9, 10]
print(f"l3 before :{l3}")

# copy from l3 to l4
l4 = l3.copy()           # deep copy - only data will get copied
print(f"l4 before :{l4}")

l4.extend([11, 12, 13])
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("=" * 60)
l5 = [2, 4, 6, 8, [5, 10, 15], 10]
print(f"l5 before :{l5}")

# copy from l5 to l6
l6 = l5.copy()      # deep copy
print(f"l6 after :{l6}")

l6[4].append(20)
l6[4].append(25)
l6[4].append(30)

print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("=" * 60)
from copy import deepcopy
l7 = [1, 2, 3, [10, 20, 30], 4, 5]
print(f"l7 before :{l7}")

# copy from l7 to l8
l8 = deepcopy(l7)       # deep copy
print(f"l8 before :{l8}")

l8[3].append(40)
l8[3].append(50)

print(f"l7 :{l7}")
print(f"l8 :{l8}")

