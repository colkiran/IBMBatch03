
print("Comparison Operators".center(60, "-"))
#  ==, >, <, >=, <=

print(f"1 == 1  :{1 == 1}")
print(f"1 == 2  :{1 == 2}")
print(f"1 > 2   :{1 > 2}")
print(f"1 < 2   :{1 < 2}")

print("Logical Operators".center(60, "-"))
# and, or, not

print(f"1 == 1 and  2 == 2 :{1 == 1 and 2 == 2}")
print(f"1 == 1 and  2 == 1 :{1 == 1 and 2 == 1}")

print(f"1 == 1 or  2 == 2  :{1 == 1 or 2 == 2}")
print(f"2 == 1 or  2 == 1  :{2 == 1 or 2 == 1}")

print(f"not(1 == 1 or  2 == 2)  :{not(1 == 1 or 2 == 2)}")
print(f"not(2 == 1 or  2 == 1)  :{not(2 == 1 or 2 == 1)}")

print("-" * 60)
print(f"ord('a') :{ord('a')}")      # integer representation of unicode character
print(f"ord('z') :{ord('z')}")
print(f"ord('A') :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")

print(f"'apple' > 'orange' :{'apple' > 'orange'}")
print(f"'apple' < 'orange' :{'apple' < 'orange'}")

print("Bitwise Operators".center(60, "-"))
print(f"5 | 3  :{5 | 3}")
print(f"5 & 3  :{5 & 3}")
print(f"5 ^ 3  :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")

print(f"16 >> 1 :{16 >> 1}")
print(f"5 >> 1  :{5 >> 1}")

print("-" * 60)
# ternary operator
age = 19
print("Eligible" if age > 18 else "Not Eligible")
