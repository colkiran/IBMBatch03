
def outerFun(flag):

    def innerFun1():

        print("Hello World")

    def innerFun2(gname):

        print(f"Greetings {gname}")

    if flag == 1:
        return innerFun1
    elif flag == 2:
        return innerFun2


infn1 = outerFun(1)
infn1()

print("-" * 60)
infn2 = outerFun(2)
infn2("Virat")