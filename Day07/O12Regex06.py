
import re

st = "baaaaat"

# res = re.match(r'ba{3}t' , st)
# res = re.match(r'ba{3,}t' , st)
res = re.match(r'ba{3,8}t' , st)

if res:
    print("Match found.....")
    print(res.group(0))         # matched string
else:
    print("Match not found.....")