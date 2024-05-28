
import mymodule as m
from mymodule import Player

print([plyr for plyr in m.players])

print("-"  * 60)

m.greet(m.gstname)

print("-"  * 60)

ply1 = Player("Sachin", 29)
print(ply1)

print("-"  * 60)

ply2 = Player("Rohit", 23)
print(ply2)