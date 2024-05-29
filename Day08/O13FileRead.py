"""
read - reads the entire contents of the file
read(no of byte) - reads the no of bytes mentioned
----------------------------------------------------------------
readline - will read one line at a time, and stores it in the buffer
readline(no of bytes) = less than or equal to the size of the line

"""
FL = open("C:\\Training\\PycharmProjects\\IBMBatch03\\Day08\\data.txt", "r")

# print("-" * 60)
# st = FL.read(1500)
# print(st)
# print("-" * 60)
#
# st = FL.readline(900)
# print(f"st :{st}")

print("-" * 60)
st = FL.readlines(855)
print(f"st :{st}")
# for line in st:
#     print(line)

FL.close()