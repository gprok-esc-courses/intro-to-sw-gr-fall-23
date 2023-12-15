
file = open("data.csv")

lines = file.readlines()

for line in lines[1:]:
    line = line.strip().split(',')
    if int(line[3]) < 10:
        print(line[1])