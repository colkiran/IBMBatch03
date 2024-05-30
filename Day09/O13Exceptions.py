
n = 10
d = 0

try:
    res = n / d
except ZeroDivisionError as z:
    print("Exception caught......")
    print(z)
except TypeError as t:
    print("Exception caught......")
    print(t)
except Exception as e:
    print("Exception caught......")
    print(e)
else:
    print(f"The quotent is :{res}")
finally:
    print("Completed the process of dividing a number....")