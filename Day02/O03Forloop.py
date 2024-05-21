
# loops
for i in range(1, 11):
    print(i, end=" ")
print()     # prints an empty new line

print("-" * 60)

for i in range(1, 30):
    # if i > 25:
    #     break       # quit  the loop
    if i % 2 == 1:
        continue    # skip the iteration
    print(i, end= " ")
else:
    print("\nCompleted the iteration........")
