
file = open("simple.txt", "r")

copy_file = open("simple-copy.txt", "a")

lines = file.readlines()

for line in lines:
    copy_file.write(line)

copy_file.close()