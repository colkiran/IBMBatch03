
import re

st = "this23234 is a sample text"

res = re.search(r'\w+', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found....")

