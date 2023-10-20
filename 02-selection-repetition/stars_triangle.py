# Print a line of stars

n = int(input("Give N: "))

for i in range(1, n+1):
    for j in range(i):
        print('*', end=' ')
    print()
print()