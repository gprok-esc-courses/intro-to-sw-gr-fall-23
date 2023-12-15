
n = int(input("Give number: "))

s = str(n)

is_palindrome = True
for i in range(len(s)):
    if s[i] != s[(i+1)*-1]:
        is_palindrome = False
        break

if is_palindrome:
    print("YES")
else:
    print("NO")