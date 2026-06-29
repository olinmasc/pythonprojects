rows = int(input("Enter rows: "))
symbol = input("Enter symbol: ")

print("\n1. Rectangle")
print("2. Left Triangle")
print("3. Inverted Triangle")
print("4. Right Triangle")
print("5. Pyramid")

choice = int(input("Enter your choice: "))

# Rectangle
if choice == 1:
    for row in range(rows):
        for column in range(rows):
            print(symbol, end=" ")
        print()

# Left Triangle
elif choice == 2:
    for row in range(rows):
        for column in range(row + 1):
            print(symbol, end=" ")
        print()

# Inverted Triangle
elif choice == 3:
    for row in range(rows):
        for column in range(rows - row):
            print(symbol, end=" ")
        print()

# Right Triangle
elif choice == 4:
    for row in range(rows):

        for column in range(rows - row - 1):
            print(" ", end=" ")

        for column in range(row + 1):
            print(symbol, end=" ")

        print()

# Pyramid
elif choice == 5:
    for row in range(rows):

        for column in range(rows - row - 1):
            print(" ", end=" ")

        for column in range(2 * row + 1):
            print(symbol, end=" ")

        print()

else:
    print("Invalid Choice")
