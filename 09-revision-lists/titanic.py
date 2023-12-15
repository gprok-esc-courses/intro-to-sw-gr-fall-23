
import csv 

# open file 
file = open("titanic.csv")

# read as Dictionaries
reader = csv.DictReader(file)

# create 2 counters, 'survived' and 'not_survived'
survived = 0
not_survived = 0

# for each row 
for row in reader:
    # if column Survived is '0'
    if row['Survived'] == '0':
        # increase 'not_survived'
        not_survived += 1
    # else
    else:
        # increase 'survived'
        survived += 1

# print counters
print("Survived: ", survived)
print("Not Survived: ", not_survived)