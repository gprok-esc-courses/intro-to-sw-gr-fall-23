# Μια βιβλιοθήκη πρέπει να παρακολουθεί τα βιβλία της. 
# Κάθε βιβλίο αντιπροσωπεύεται από το ISBN, τον τίτλο, 
# τους συγγραφείς και μια κατηγορία.
# Ποια δομή δεδομένων ταιριάζει καλύτερα;
# Γράψτε ένα πρόγραμμα για τη φόρτωση δεδομένων βιβλίου 
# από ένα αρχείο CSV και, στη συνέχεια, 
# δώστε επιλογές για αναζήτηση κατά ISBN, 
# λέξη-κλειδί στον τίτλο ή κατηγορία.

import csv

file = open("books.csv")
reader = csv.DictReader(file)

books = {}

for row in reader:
    books[row['isbn']] = row

print(books)

for key in books:
    print(books[key])

for key, value in books.items():
    print(value)


