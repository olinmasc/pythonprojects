# Python Quiz Game

questions = (
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "What is the chemical symbol for gold?"
)
options = (
    ("A. Paris", "B. London", "C. Berlin", "D. Madrid"),
    ("A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"),
    ("A. Ag", "B. Au", "C. Al", "D. Pb")
)
answers = (
    "A",
    "B",
    "B"
)
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print("-------------------------")
print("RESULTS")
print("-------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("\nGuesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"\nYour score is: {score}%")
