
class TooTiny(Exception):
    pass

class TooYoung(Exception):
    pass

class ToOld(Exception):
    pass

age = 25

try:
    if age < 6:
        raise TooTiny("Too very young to vote...")
    elif age < 18:
        raise TooYoung("Very young to cast the vote.....")
    elif age > 100:
        raise ToOld("Very old to cast the vote....")
    else:
        print("You can cast your valuable vote......")
except TooTiny as t:
    print(t)
except TooYoung as y:
    print(y)
except ToOld as o:
    print(o)
finally:
    print("Completed the process of voting.....")