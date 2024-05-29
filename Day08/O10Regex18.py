import re

dt = "15-02 \/1998"

res = re.search(r'([0-2][1-9]|[1-3][0-1])(\/|-)(0[1-9]|1[0-2])\2(?!0000)([0-9]{4})', dt)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found....")
