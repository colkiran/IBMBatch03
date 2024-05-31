
def fun():
   x = 1
   print("apples from ooty.....")
   yield x
   x += 9
   print("Oranges from kanpur....")
   yield x
   x += 10
   print("Grapes from hubli......")
   yield x

res = fun()
print(f"res :{res}")

print("-" * 60)
print(res.__next__())

print("-" * 60)
print(res.__next__())

print("-" * 60)
print(res.__next__())

# print("-" * 60)
# print(res.__next__())
