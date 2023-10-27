invoices = [34, 19, 90, 65, 18, 54]

max = 0
min = float('inf')
total = 0

print(len(invoices))

# for i in range(len(invoices)):
#     print(invoices[i])

for invoice in invoices:
    total += invoice
    if invoice > max:
        max = invoice
    if invoice < min:
        min = invoice

print("MAX", max)
print("MIN", min)
print("TOTAL", total)
print("AVG", total/len(invoices))