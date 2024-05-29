
import re

st = "this232343423423 is a sample text"

res = re.search(r'\d{5}', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found....")

