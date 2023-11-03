
list2d = [
    [1, 2, 3, 4, 22, 23, 34],
    [5, 6, 7, 8],
    [9, 10, 11, 12, 18],
    [123, 124]
]

print(len(list2d))
print(len(list2d[1]))

# print(list2d[1][3])

for row in range(len(list2d)):
    for col in range(len(list2d[row])):
        print(list2d[row][col], end=' ')
    print()