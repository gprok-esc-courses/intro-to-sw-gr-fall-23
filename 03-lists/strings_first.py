s = "Python Is An Easy Language!"

print(len(s))
print(s[0])
print(s[len(s)-1])
print(s[-1])
print(s[3:15])
print(s[:10])
print(s[15:])

print(s.upper())
print(s.lower())

if 'asdasdasd' in s.lower():
    print(s.index('asdasdasd'))
    print("Found")

ch = input("Give a character: ")

ch2 = ch.lower()
s2 = s.lower()

counter = 0
for c in s2:
    if c == ch2:
        counter += 1

print(counter)

print(s2.count(ch2))

print(s2.index(ch2, 15))