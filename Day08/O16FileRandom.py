
FL = open("data.txt", "rb")

pos = FL.seek(50, 0)
print(F"Position :{pos}")

pos = FL.seek(75, 1)
print(F"Position :{pos}")

pos = FL.seek(200, 2)
print(F"Position :{pos}")

pos = FL.seek(0, 2)
print(F"Position :{pos}")

# pos = FL.seek(-10, 0)

FL.close()