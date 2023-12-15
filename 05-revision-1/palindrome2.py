
n = int(input("Give number: "))

s = str(n)
rs = s[::-1]

print(s)
print(rs)

if s == rs:
    print("YES")
else:
    print("NO")