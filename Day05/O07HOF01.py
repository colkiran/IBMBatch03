
def callMe():
    print("Apples from ooty......")

def fun(fnc):
    print("Hello....")
    fnc()
    print("Hi.......")
    print("-" * 60)

    def defineMe():
        print("Oranges from Kanpur......")

    return defineMe

def funCallBack(fnc):
    print("Mera bharath Mahan.....")
    fnc()
    print("India is great......")


funCallBack(fun(callMe))



