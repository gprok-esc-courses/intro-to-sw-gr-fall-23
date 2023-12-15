import csv

file = open("data.csv")
reader = csv.reader(file)

counter = 0
for row in reader:
    if counter != 0 and int(row[3]) < 10:
        print(row[1])
    counter += 1