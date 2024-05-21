
print("Append".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(F"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)

print(f"l1 :{l1}")
l1.append([9, 10, 11, 12, 13])

print(f"l1 :{l1}")
print(l1[8])
print(l1[8][1:4])

print("extend".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.extend([6, 7, 8])
print(f"l1 :{l1}")

# l1.extend(9)
print("insert".center(60,  "-"))
l1 = [6, 7, 8, 9 ,10]
print(f"l1 :{l1}")
l1.insert(0, 5)
l1.insert(0, 4)
l1.insert(0, 3)

l1.insert(8, 11)
print(f"l1 :{l1}")
