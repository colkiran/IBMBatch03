
import csv
from prettytable import PrettyTable

with open("Employee.csv", "r") as CSVR:
    emp_details = csv.reader(CSVR)
    prtyTbl = PrettyTable(next(emp_details))


    for rec in emp_details:
       prtyTbl.add_row(rec)

print(prtyTbl)

