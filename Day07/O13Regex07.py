
import re

st = "bgt"

# res = re.match(r'b[a-zA-Z0-9]t' , st)
# res = re.match(r'b[aeiou]t' , st)
res = re.match(r'b[^aeiou]t' , st)

if res:
    print("Match found.....")
    print(res.group(0))         # matched string
else:
    print("Match not found.....")