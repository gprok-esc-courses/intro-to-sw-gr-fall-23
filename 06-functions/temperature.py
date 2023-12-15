# Ask user for a value representing a temperature.
# Then ask a letter indicating the type, 
# C for Celsius or F for Fahrenheit. 
# Then convert if C convert to F 
# [formula: F = (C * 9/5) + 32], 
# or from F to C 
# [formula: C = 5 / 9 * (F - 32)].

def convert_temperature(t, type):
    if type == "C":
        return t * 9 / 5 + 32
    elif type == "F":
        return  5 / 9 * (t - 32)
    else:
        return None 

def celcius2farenheit(c: float) -> float:
    return c * 9 / 5 + 32

def farenheit2celcius(f):
    return  5 / 9 * (f - 32)

if __name__ == "__main__":
    temperature = float(input("Give Temperature: "))
    type = input("Give Type (C or F): ")

    if type == "C":
        f = celcius2farenheit(temperature)
        print("F", f)
    elif type == "F":
        c = 5 / 9 * (temperature - 32)
        print(c)
    else:
        print("Wrong type", type)