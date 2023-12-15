# Προσλαμβάνεστε για να δημιουργήσετε μια εφαρμογή 
# για προσωπική διαχείριση εργασιών. Οι εργασίες 
# μπορεί να είναι open, blocked, in progress, or completed. 
# Ο χρήστης θα μπορεί να προσθέτει εργασίες, να βλέπει τις 
# εργασίες με βάση την κατάστασή τους και να τις επισημαίνει 
# ανάλογα.
# Ποια δομή δεδομένων θα χρησιμοποιήσετε;

tasks = {}
tasks[1] = {'id': 1, 'descr': 'Buy laptop', 'status': 'open'}
tasks[2] = {'id': 2, 'descr': 'Fix printer', 'status': 'in progress'}
tasks[3] = {'id': 3, 'descr': 'Check email', 'status': 'closed'}
tasks[4] = {'id': 4, 'descr': 'Debug app', 'status': 'blocked'}
next = 5

def display_menu():
    print("1. Add task")
    print("2. Open tasks")
    print("3. Blocked tasks")
    print("4. In Progress tasks")
    print("5. Closed tasks")
    print("6. Change status")
    print("0. EXIT")

def add_task(tasks, next):
    descr = input("Description: ")
    task = {'id': next, 'descr': descr, 'status': 'open'}
    tasks[next] = task
    next += 1
    return tasks, next

def print_by_status(tasks, status):
    for key, value in tasks.items():
        if value['status'] == status:
            print(value)

def change_status(tasks):
    statuses = ["open", "blocked", "in progress", "closed"]
    id = int(input("Give ID: "))
    if id in tasks:
        status = input("Give new status: ")
        if status in statuses:
            tasks[id]['status'] = status
        else:
            print("Invalid status")
    else:
        print("ID not found")
    return tasks


while True:
    display_menu()
    try:
        choice = int(input("Select: "))
        if choice == 1:
            tasks, next = add_task(tasks, next)
        elif choice == 2:
            print_by_status(tasks, 'open')
        elif choice == 3:
            print_by_status(tasks, 'blocked')
        elif choice == 4:
            print_by_status(tasks, 'in progress')
        elif choice == 5:
            print_by_status(tasks, 'closed')
        elif choice == 6:
            tasks = change_status(tasks)
            print(tasks)
        elif choice == 0:
            break
        else:
            print("Wrong choice")
    except ValueError:
        print("Wrong choice")