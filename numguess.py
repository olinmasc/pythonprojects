# Number guessing game
import random

lower_bound = 1
upper_bound = 100
number_to_guess = random.randint(lower_bound, upper_bound)
guesses = 0
print(f"Welcome to the Number Guessing Game!")
print(
    f"I'm thinking of a number between {lower_bound} and {upper_bound}. Can you guess what it is?")
while True:
    guess = input("Enter your guess (or type 'exit' to quit): ")
    if guess.lower() == 'exit':
        print("Thanks for playing! Goodbye!")
        break
    elif not guess.isdigit():
        print("Invalid input. Please enter a valid number.")
    else:
        guess = int(guess)
        guesses += 1

        if guess < lower_bound or guess > upper_bound:
            print(
                f"Please guess a number between {lower_bound} and {upper_bound}.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(
                f"Congratulations! You've guessed the number {number_to_guess} in {guesses} guesses!")
            break
