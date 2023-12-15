
file = open("simple.txt")

lines = file.readlines()

for line in lines:
    print(line.strip())