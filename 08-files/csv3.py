import csv 

file = open("data.csv")

reader = csv.DictReader(file)

total = 0
for row in reader:
    print(row)
    total += float(row['price'])

print(total)