# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input(
        "Enter the name of the food item (or type 'done' to finish): ")
    if food.lower() == 'done':
        break
    price = float(input(f"Enter the price of {food}: "))
    foods.append(food)
    prices.append(price)
    total += price
print("\nShopping Cart Summary:")

for food in foods:
    print(food, end=" ")

print(f"\nTotal: ${total:.2f}")
