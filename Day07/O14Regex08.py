
import re

st = "boat"

res = re.match(r'b(oa|ai)t' , st)

if res:
    print("Match found.....")
    print(res.group(0))         # matched string
else:
    print("Match not found.....")