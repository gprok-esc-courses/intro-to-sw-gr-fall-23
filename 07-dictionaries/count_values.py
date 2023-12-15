data = ["Peter", "John", "Mary", "Mike", "John",
        "Ann", "Mary", "John", "Peter", "Tom"]

names = {}

for name in data:
    if name in names:
        names[name] += 1
    else:
        names[name] = 1

for key in names:
    print(key, names[key])