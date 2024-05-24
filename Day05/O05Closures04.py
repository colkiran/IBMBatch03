

def outerFun(greet):

    def innerFun(sep):

        def innerMost(gname):
            from emojis import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)

        return innerMost
    return innerFun

engGrt = outerFun("Welcome")
engGrtTiger = engGrt("bear")
engGrtTiger("Prabakar")

"""
engGrt = outerFun("Welcome")
engGrtDblArw = engGrt("======>>")
kanGrt = outerFun("Namaskara")
kanGrtSngArw = kanGrt("------->")

engGrtDblArw("Steven")
kanGrtSngArw("Srinath")
"""





