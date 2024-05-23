
# non local variables

def outerFun():
    gname = "Sachin"
    def innerFun():
        nonlocal gname      # only local variable can be converted into nonlocal variables

        gname = "Mr." + gname
        print("Hello World")
        print(f"Greetings {gname}")

    innerFun()
    print(f"outer :{gname}")

outerFun()
