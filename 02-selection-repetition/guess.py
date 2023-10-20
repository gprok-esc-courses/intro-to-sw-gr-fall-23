# Game: Guess the number
import random

secret = random.randint(1, 100)
print(secret)
answer = 0

while answer != secret:
    answer = int(input("Guess: "))
    if answer > secret:
        print("Go DOWN")
    elif answer < secret:
        print("Go UP")
    else: 
        print("Congrats!")
