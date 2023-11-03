# Στη λίστα της άσκησης 3, μπορείτε να βρείτε αν 
# αυτή περιέχει διπλοεγγραφές (δηλαδή αν έχει έστω 
# και έναν αριθμό που εμφανίζεται 2 ή περισσότερες φορές);

import random 

values = []
for i in range(30):
    n = random.randint(1, 100)
    values.append(n)


svalues = sorted(values)
print(svalues)

for i in range(len(svalues) - 1):
    if svalues[i] == svalues[i+1]:
        print(svalues[i])

# another approach, sublist
print("Using sublist")
for i in range(len(svalues) - 1):
    if svalues[i] in svalues[i+1:]:
        print(svalues[i])