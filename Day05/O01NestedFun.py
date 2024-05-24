
def outerFun():
    gname = "Jack"
    def innerFun():

        print("Hello World")
        print(f"Greeting Mr.{gname}, Welcome to the event......")

    innerFun()

outerFun()

