# Temperature Conversion Program

unit = input("Enter unit (C or F): ")
temperature = float(input("Enter temperature: "))

if unit.upper() == "C":
    converted_temp = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {converted_temp:.2f}°F.")
elif unit.upper() == "F":
    converted_temp = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {converted_temp:.2f}°C.")
else:
    print("Invalid unit. Please enter 'C' or 'F'.")
