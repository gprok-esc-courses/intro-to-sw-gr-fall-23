# Find if a number is prime or not

n = int(input("Give a number: "))

# I assume that the number is prime
is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not prime")