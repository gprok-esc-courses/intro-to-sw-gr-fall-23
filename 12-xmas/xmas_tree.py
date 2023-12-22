# User gives a number n
# Print a xmas tree with the base equal to n
# If number n is even, subtract 1
# Add random O as xmas balls, with a probability of 20%

import random


def print_tree_base(base_height: int, tree_height: int) -> None:
    """
    Prints the base of a xmas tree, using a # char with the 
    specified height.
    """
    for b in range(base_height):
        for i in range(tree_height // 2):
            print(' ', end='')
        print('#')

def print_tree_row(spaces: int, asterisks: int, probability: int) -> None:
    """
    Prints a row of the xmas tree.
    First prints spaces and then asterisks to the specified values.
    Also adds random decoration according to the probability.
    """
    for s in range(spaces):
        print(' ', end='')
    for a in range(asterisks):
        p = random.randint(1, 100)
        if p < probability:
            print('O', end='')
        else:
            print('*', end='')
    print()


try:
    n = int(input("Give n: "))
except ValueError:
    print("Integer required, setting n to default value 7")
    n = 7

if n % 2 == 0:
    n -= 1

lines = n // 2 + 1
spaces = n // 2
asterisks = 1
probability = 20

# Loop lines times
    # Loop spaces times and print a space
    # Loop asterisks times and print an asterisk
    # Decrease spaces by 1
    # Increase asterisks by 2

for i in range(lines):
    print_tree_row(spaces, asterisks, probability)
    spaces -= 1
    asterisks += 2

print_tree_base(2, n)
