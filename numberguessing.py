# Number Guessing Game
import random

print("Welcome to the Number Guessing Game!")

# Start the game
while True:
    start = input("Type 'start' to begin: ").lower()
    if start == "start":
        break
    else:
        print("You need to type 'start' to play!")

# Get min and max numbers
while True:
    try:
        min_number = int(input("Enter the minimum number: "))
        max_number = int(input("Enter the maximum number: "))
        if min_number >= max_number:
            print("Minimum must be less than maximum. Try again.")
        else:
            break
    except ValueError:
        print("Please enter valid integers.")

# Generate random number
target_number = random.randint(min_number, max_number)

# Start guessing
attempts = 0
while True:
    try:
        guess = int(input("Your guess: "))
        attempts += 1
        if guess < target_number:
            print("Go higher!")
        elif guess > target_number:
            print("Go lower!")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break
    except ValueError:
        print("Please enter a valid integer.")
