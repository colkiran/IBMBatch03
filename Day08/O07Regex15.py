
import re

st = "thiS Is a sample text"

res = re.search(r'\bis', st, re.I)
# res = re.search(r'\Bis', st, re.I)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found....")

