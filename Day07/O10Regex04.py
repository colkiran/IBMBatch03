
import re

st = "bt"

res = re.match(r'ba?t' , st)

if res:
    print("Match found.....")
    print(res.group(0))         # matched string
else:
    print("Match not found.....")