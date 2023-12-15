import csv 

file = open("data.csv")

reader = csv.reader(file)

for row in reader:
    print(row)