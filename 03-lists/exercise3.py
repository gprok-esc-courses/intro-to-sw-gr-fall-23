# Δημιουργήστε μια λίστα και προσθέστε σε αυτήν 
# 100 τυχαίους αριθμούς, στην κλίμακα από 1 έως 1000. 
# Στη συνέχεια βρείτε το μικρότερο, μεγαλύτερο, 
# το άθροισμα και τον μέσο όρο.
import random 

values = []
for i in range(100):
    n = random.randint(1, 1000)
    values.append(n)

print(values)


# max_v = 0
# for v in values:
#     if v > max_v:
#         max_v = v
# print(max_v)
print(max(values))
print(min(values))
print(sum(values))
print(sum(values)/100)