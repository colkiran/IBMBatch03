
def outerFun(greet):

    def innerFun(gname):

        print(greet, gname)

    return innerFun

outerFun("Welcome")("Sachin")

print("-" * 60)

engGrt = outerFun("Welcome")
kanGrt = outerFun("Namaskara")

# simple curry
engGrt("Rahul")
kanGrt("Kumble")

