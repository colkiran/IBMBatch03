
# HOF - if a function takes another function as an argument or returns a function as a reference

def fun(*args):
    print(*args)

fun()
fun(10)
fun(10, 20)
fun(10, 20, 30)

print("-" * 60)
def sum(x, y):
    return x + y

def diff(x, y):
    return x - y

def log_details(fnc):
    logInfo = "Logging into the service....."

    def helper(*args):
        print(logInfo)
        print(fnc(*args))
        print("-" * 60)

    return helper


sumlogger = log_details(sum)
sumlogger(45, 85)

difflogger = log_details(diff)
difflogger(90, 17)
