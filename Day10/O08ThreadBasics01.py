import time

def fun(x):
    print("function going to sleep....")
    time.sleep(x)
    print("function just woke up.....")

print("function called....")
s = time.perf_counter()
fun(2)
fun(2)
fun(2)
fun(2)
fun(2)
e = time.perf_counter()
print("execution completed.....")
print(f"Total time taken :{round(e - s, 2)}")

