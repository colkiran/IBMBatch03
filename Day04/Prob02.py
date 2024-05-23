
from calendar import month_abbr

months = ['dec', 'aug', 'apr', 'jun', 'sep', 'mar', 'oct', 'jan', 'nov', 'may', 'jul', 'feb']

print(f"unsorted months :{months}")

print("-" * 60)

print(list(month_abbr))

res = sorted(months, key=list(map(lambda mth: mth.lower(), list(month_abbr))).index)

print(F"Sorted Months :{res}")

"""
lambda x: x ** 2

res = sorted(cal, key=list(map(lambda mth: mth.lower(), list(month_abbr))).index)
"""