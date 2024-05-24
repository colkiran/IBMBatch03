
def outerFun():
    gname = "Jack"
    def innerFun():

        print("Hello World")
        print(f"Greeting Mr.{gname}, Welcome to the event......")

    return innerFun

outerFun()()    # calls the innerFun directly

print("-" * 60)

innref = outerFun()
innref()