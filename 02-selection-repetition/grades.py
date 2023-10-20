# Give a message according to the grade of a student

grade = float(input("Give your grade: "))

if grade >= 70:
    print("Exeptional!")
elif grade >= 60:
    print("Very good")
elif grade >= 50:
    print("Good")
elif grade >= 40:
    print("Fair")
else:
    print("Fail")