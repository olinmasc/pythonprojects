# Concession Stand

menu = {
    "hot dog": 2.50,
    "hamburger": 3.00,
    "fries": 1.50,
    "soda": 1.00,
}

cart = []
total = 0.0

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

while True:
    item = input(
        "Enter an item to add to your cart (or 'done' to finish): ").lower()
    if item == "done":
        break
    elif item in menu:
        cart.append(item)
        total += menu[item]
        print(f"Added {item} to your cart. Current total: ${total:.2f}")
    else:
        print("Item not found in the menu. Please try again.")

print(f"Final total: ${total:.2f}")
