# Rock Paper Scissors Game
import random

options = ["rock", "paper", "scissors"]
print("Welcome to Rock, Paper, Scissors!")
while True:
    player = input(
        "Enter your choice (rock, paper, scissors) or 'exit' to quit: ").lower()
    if player == "exit":
        print("Thanks for playing! Goodbye!")
        break
    elif player not in options:
        print("Invalid choice. Please try again.")
    else:
        computer = random.choice(options)
        print(f"Computer chose: {computer}")

        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win!")
        else:
            print("You lose!")
