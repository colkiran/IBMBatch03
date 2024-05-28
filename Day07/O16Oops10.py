
import re

st = "LCNO-TLG-08-2008-0001"

res = re.search(r'LCNO-(KAR|KER|APN|TND|TLG|MAH)-([0-6][1-9]|[1-7][0-3])-([2-9][0-9]{3})-(?!0000)([0-9]{4})' , st)

if res:
    print("Match found.....")
    print(res.group(0))         # matched string
else:
    print("Match not found.....")