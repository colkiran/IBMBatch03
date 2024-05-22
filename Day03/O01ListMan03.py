
print("pop".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(7)
print(f"res :{res}")

res = l1.pop(3)
print(f"res :{res}")

res = l1.pop()
print(f"res :{res}")

print(f"l1 :{l1}")

print("remove".center(60, "-"))
l2 = [1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 2, 3, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2]
print(f"l2 :{l2}")

l2.remove(3)
l2.remove(3)
l2.remove(3)

print(f"l2 :{l2}")
# remove all 2's from the list

print("-" * 60)
while (2 in l2):
    l2.remove(2)

print(f"l2 :{l2}")

print("clear".center(60, "-"))
l1 = list(range(10, 101, 10))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")

print("count".center(60,"-"))
l2 = [1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 2, 3, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2]
print(f"l2 :{l2}")

print(f"1 :{l2.count(1)}")
print(f"2 :{l2.count(2)}")
print(f"3 :{l2.count(3)}")
print(f"5 :{l2.count(5)}")

print("index".center(60, "-"))
l2 = [1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 2, 3, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2]
print(f"l2 :{l2}")

print(f"1st 3 :{l2.index(3)}")
print(f"2nd 3 :{l2.index(3, l2.index(3) + 1)}")
print(f"3rd 3 :{l2.index(3, l2.index(3, l2.index(3) + 1) + 1)}")
