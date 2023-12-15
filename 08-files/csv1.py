
file = open("data.csv")

lines = file.readlines()

headers = lines[0].strip().split(',')
data = []
dict = {}
for i in range(1, len(lines)):
    order = lines[i].strip().split(',')
    data.append(order)
    dict[order[0]] = {"descr": order[1], "price": order[2]}
    

print(headers)
print(data)
print(dict)