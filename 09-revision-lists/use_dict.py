import csv

file = open("data.csv")
reader = csv.DictReader(file)

for row in reader:
    # print(row)
    if int(row['stock']) < 10:
        print(row['name'])