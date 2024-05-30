
import json

player = {
    'players':[
        {'id': 'P101', 'Name': 'Sachin Tendulkar', 'Matches': 585, 'runs': 28500, 'age': 38},
        {'id': 'P102', 'Name': 'Sourav Ganguly', 'Matches': 430, 'runs': 19400, 'age': 36},
        {'id': 'P103', 'Name': 'Rahul Dravid', 'Matches': 390, 'runs': 18500, 'age': 35},
        {'id': 'P104', 'Name': 'Virendra Sehwag', 'Matches': 410, 'runs': 23500, 'age': 34},
        {'id': 'P105', 'Name': 'VVS Laxman', 'Matches': 298, 'runs': 15500, 'age': 36},
        {'id': 'P106', 'Name': 'Virar Kholi', 'Matches': 450, 'runs': 23000, 'age': 38},
        {'id': 'P107', 'Name': 'Yuvraj Singh', 'Matches': 520, 'runs': 19400, 'age': 36},
        {'id': 'P108', 'Name': 'MS Dhoni', 'Matches': 460, 'runs': 18500, 'age': 35},
        {'id': 'P109', 'Name': 'Md Kaif', 'Matches': 345, 'runs': 12400, 'age': 34},
        {'id': 'P110', 'Name': 'Suresh Raina', 'Matches': 410, 'runs': 15500, 'age': 36},
    ]
}

JFW = open("IndianTeam.json", "w")
json.dump(player, JFW, indent=4)
JFW.close()

print("-" * 60)
empdata = {'name': 'Kevin', 'age': 32, 'city': 'NewYork'}
print(empdata)
print(type(empdata))

res = json.dumps(empdata)
print(res)
print(type(res))