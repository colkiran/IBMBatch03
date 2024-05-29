

import re

st = "this is a sample text"

res = re.search(r'\s', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found....")

