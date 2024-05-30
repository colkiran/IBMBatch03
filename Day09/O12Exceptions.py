
import sys

n = 10
d = "4"

try:
    res = n / d
except:
    print("Exception caught......")
    print(sys.exc_info()[0])        # class name
    print(sys.exc_info()[1])        # message
else:
    print(f"The quotent is :{res}")
finally:
    print("Completed the process of dividing a number....")