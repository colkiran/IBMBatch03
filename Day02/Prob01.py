
print( "Prime Number between 150 to 50 ")
n = 0
for num in range(150, 50 ,-1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num,end=" ")
           n += 1

print(f"\nThere are {n} prime numbers between 150 and 50")