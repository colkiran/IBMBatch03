
import re

st = "bat"

res = re.match(r'b.t' , st)

if res:
    print("Match found.....")
    print(res.group(0))         # matched string
else:
    print("Match not found.....")