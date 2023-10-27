invoices = [34, 19, 90, 65, 18, 54]

last = len(invoices) - 1

for i in range(len(invoices) - 1):
    for j in range(last):
        if invoices[j] > invoices[j+1]:
            # temp = invoices[j]
            # invoices[j] = invoices[j+1]
            # invoices[j+1] = temp 
            invoices[j], invoices[j+1] = invoices[j+1], invoices[j]

print(invoices)