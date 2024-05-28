
import sys
import gurgaon.mymodule as m
from gurgaon.mymodule import Player

for path in sys.path:
    print(path)

print("-" * 60)

m.greet("Sehwag")

ply1 = Player("Lara", 34)
print(ply1)