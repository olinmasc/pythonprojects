# Compound Interest Calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount (greater than 0): "))
    if principle <= 0:
        print("Principle amount must be greater than 0. Please try again.")

while rate <= 0:
    rate = float(input("Enter the rate of interest (greater than 0): "))
    if rate <= 0:
        print("Rate of interest must be greater than 0. Please try again.")

while time <= 0:
    time = float(input("Enter the time period in years (greater than 0): "))
    if time <= 0:
        print("Time period must be greater than 0. Please try again.")

compound_interest = principle * (1 + rate / 100) ** time
print(
    f"The compound interest for a principle amount of {principle}, at a rate of {rate}% over {time} years is: {compound_interest:.2f}")
