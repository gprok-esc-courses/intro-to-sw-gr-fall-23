
names = ["Peter", "Paul", "Mary", "Ann",
         "John", "William", "Sue", "Mike"]

ch = input("Type a character: ")

counter = 0
for name in names:
    if name[0].lower() == ch.lower():
        print(name)
        counter = counter + 1

if counter == 0:
    print("No names found")