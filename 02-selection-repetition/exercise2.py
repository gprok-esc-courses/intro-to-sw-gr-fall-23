# Ask user for a value representing a temperature.
# Then ask a letter indicating the type, 
# C for Celsius or F for Fahrenheit. 
# Then convert if C convert to F 
# [formula: F = (C * 9/5) + 32], 
# or from F to C 
# [formula: C = 5 / 9 * (F - 32)].

temperature = float(input("Give Temperature: "))
type = input("Give Type (C or F): ")

if type == "C":
    f = temperature * 9 / 5 + 32
    print("F", f)
elif type == "F":
    c = 5 / 9 * (temperature - 32)
    print(c)
else:
    print("Wrong type", type)