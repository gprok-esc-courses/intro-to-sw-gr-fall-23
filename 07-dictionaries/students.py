students = {}

students[1022] = {"name": "Mike", "grade": 34}
students[1190] = {"name": "Peter", "grade": 75}
students[1287] = {"name": "Mary", "grade": 47}
students[1001] = {"name": "Ann", "grade": 63}
students[2090] = {"name": "Lisa", "grade": 78}
students[1002] = {"name": "John", "grade": 47}
students[1191] = {"name": "Tom", "grade": 49}

# Print all students with grade less than 50
for id in students:
    if students[id]['grade'] < 50:
        print(students[id]['name'])