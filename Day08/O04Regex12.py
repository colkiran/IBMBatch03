
import re

st = "this@#$%^&*23234 is a sample text"

res = re.search(r'\S+', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found....")

