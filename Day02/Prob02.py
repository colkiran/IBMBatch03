
for i in range(5, 0, -1):
    for k in range(1, 6-i):
        print(" ", end="")
    for j in range(1, i+1):
        print(j, end = " ")
    print()

for i in range(2, 6):
    for k in range(1, 6-i):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end = " ")
    print()