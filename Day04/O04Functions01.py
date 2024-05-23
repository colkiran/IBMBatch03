
def greet():
    print("Greeting Mr.Sachin, Welcome to the event........")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event......")

# city is a default argument and gname is a non default argument
def greetGstCty(gname, city = "Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event......")

greet()

print("-" * 60)
greetGst("Rahul")
greetGst("Sehwag")

print("-" * 60)
greetGstCty("Sachin")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

print("-" * 60)

def myproduct(x, y):
    return x * y

print(" %i * %i = %i" % (10, 20, myproduct(10, 20)))

# how many return values can a function have - one
from collections import namedtuple
def ArithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    nmdTpl = namedtuple("Arith", "s d p q")
    arith = nmdTpl(s = sum, d = diff, p = prod, q = quot)
    # return sum, diff, prod, quot
    return arith

# res = ArithCalc(20, 8)
# print(f"res :{res}")

res = ArithCalc(20, 8)
print(f"res :{res}")
print(f"Sum  :{res.s}")
print(f"Diff :{res.d}")
print(f"Prod :{res.p}")
print(f"Quot :{res.q}")

print("-" * 60)
# variable length arguments = *args and **kwargs

def productAll(*numbers):
    print(numbers)
    print(*numbers)
    prod = 1
    for number in numbers:
        prod *=  number
    return prod

res = productAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)
def extractDetails(**details):
    print(details)
    for k, v in details.items():
        print(k,  "=>", v)

extractDetails(name='sachin', age=32, runs=135, oppn="SA", venue="Dublin")

print("-" * 60)
# doc string

def fun():
    # this is a comment
    "This is docstring"
    print("Hello World")

fun()
print(fun.__doc__)

print("-" * 60)
def fun1(x, y):
    """
    fun1
    ----
    1. if  x and y are integers then the result would be the sum of x and y
    2. if x and y are strings theb the result would be a concatenated string of x and y
    3. if x and y are of two different data types then the result would be an error
    """
    return x + y

print(fun1(10, 20))
print(fun1("hello", "world"))

help(fun1)
