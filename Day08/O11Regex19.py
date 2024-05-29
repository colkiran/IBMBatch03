"""
1. string that didn't match the regex
2. string that matched the regex
3. string that is not checked
"""

import re

st = "the quick brown fox jumps ove the lazy dog"

res = re.search(r'fox', st)

if res:
    print("Match found.....")
    print(f"String that didn't match regex :{st[:res.start()]}")
    print("String that matched : {reres.group(0)}")
    print(f"Strm yet to be checked : {st[res.end():]}")
else:
    print("Match not found....")

