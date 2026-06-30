# Dice Roller program

import random

dice_art = {
    1: (
        "┌───────────────┐",
        "│               │",
        "│       ●       │",
        "│               │",
        "└───────────────┘"
    ),
    2: (
        "┌───────────────┐",
        "│   ●           │",
        "│               │",
        "│           ●   │",
        "└───────────────┘"
    ),
    3: (
        "┌───────────────┐",
        "│   ●           │",
        "│       ●       │",
        "│           ●   │",
        "└───────────────┘"
    ),
    4: (
        "┌───────────────┐",
        "│   ●       ●   │",
        "│               │",
        "│   ●       ●   │",
        "└───────────────┘"
    ),
    5: (
        "┌───────────────┐",
        "│   ●       ●   │",
        "│       ●       │",
        "│   ●       ●   │",
        "└───────────────┘"
    ),
    6: (
        "┌───────────────┐",
        "│   ●       ●   │",
        "│   ●       ●   │",
        "│   ●       ●   │",
        "└───────────────┘"
    )
}

dice = []
total = 0
num_of_dice = int(input("Enter the number of dice to roll: "))
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))
    for line in dice_art[dice[die]]:
        print(line)
    total += dice[die]

print(f"Total: {total}")
