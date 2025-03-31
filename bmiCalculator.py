weight = float(input("Weight:"))

# Loop until the user provides a valid unit
while True:
    unit = input("K(g) or L(bs):").upper()
    if unit in ["K", "L"]:
        break
    print("Invalid input! Please enter 'K' for Kilogram and 'L' for Pounds.")
C:\Users\DELL\PycharmProjects\PythonProject\bmiCalculator.py
# Perform conversion based on valid input
if unit.upper() == "K":
    converted = weight/0.45
    print("Weight in L(bs): " + "{:.2f}".format(converted))
else:
    converted = weight * 0.45
    print("Weight in K(g): " + "{:.2f}".format(converted))