# Write a program to produce some basic statistics
# on sales. Ask user how many invoices were issued
# today, then repeat and ask the amount of each 
# invoice. In the end display the maximum and 
# minimum value, the total value, and the average.

invoices = int(input("Num of Invoices: "))
max = 0
min = float('inf')
total = 0

for i in range(invoices):
    amount = float(input("Give amount " + str(i+1) + ": "))
    total += amount
    if amount > max:
        max = amount
    if amount < min:
        min = amount

print("MAX", max)
print("MIN", min)
print("TOTAL", total)
print("AVG", total/invoices)