
import sys

# print(sys.path)
sys.path.append("C:/Delhi")
for path in sys.path:
    print(path)

import gurgaon.mymodule as m
from gurgaon.mymodule import Player
m.greet("Sourav")

ply1 = Player("Rahul", 32)
print(ply1)
