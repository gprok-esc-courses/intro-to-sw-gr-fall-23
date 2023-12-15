import csv

file = open("uefa.csv")
reader = csv.DictReader(file)

teams = {}

for row in reader:
    code = row['code']
    if code in teams:
        teams[code] += 1
    else:
        teams[code] = 1

for key in teams:
    print(key, teams[key])
