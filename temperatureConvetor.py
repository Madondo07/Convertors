temp = float(input("Temperature: "))

# Loop until the user provides a valid unit
while True:
    unit = input("Celsius(ºC) or Fahrenheit(ºF): ").upper()
    if unit in ["C", "F"]:
        break
    print("Invalid input! Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Perform conversion based on valid input
if unit == "C":
    convertedTemp = (temp * 0.18) + 32
    print("\nTemperature in Fahrenheit(ºF): " + "{:.2f}".format(convertedTemp))
else:
    convertedTemp = (temp - 32) / 0.18
    print("\nTemperature in Celsius(ºC): " + "{:.2f}".format(convertedTemp))