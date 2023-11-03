# Δημιουργήστε μια άδεια λίστα: usernames = [] η οποία θα τηρεί τα usernames μιας εφαρμογής. Στη συνέχεια δημιουργήστε ένα menu με τις εξής επιλογές:
# 1. Register User
# 2. Delete account
# 0. EXIT
# Επιλογή 1: Ζητήστε ένα username από τον χρήστη, αν δεν υπάρχει ήδη στη λίστα, προσθέστε το και δείξτε ανάλογο μήνυμα. Αν υπάρχει δείξτε μήνυμα ότι δεν μπορεί να χρησιμοποιηθεί.
# Επιλογή 2: Ζητήστε ένα username από τον χρήστη, αν υπάρχει ήδη στη λίστα, διαγράψτε το και δείξτε κατάλληλο μήνυμα. Αν δεν υπάρχει δείξτε μήνυμα ότι το username δεν βρέθηκε.
# Επιλογή 0: Τερματισμός του προγράμματος.

usernames = []

while True:
    print("1. Register User")
    print("2. Delete account")
    print("0. EXIT")
    choice = int(input("Choose: "))

    if choice == 1:
        username = input("Give username: ")
        if username in usernames:
            print("Username already in list")
        else:
            usernames.append(username)
            print("Username added")
    elif choice == 2:
        username = input("Give username: ")
        if username in usernames:
            usernames.remove(username)
            print("Username deleted")
        else:
            print("Username not found")
    elif choice == 0:
        print("Bye!")
        break
    else:
        print("Wrong choice")