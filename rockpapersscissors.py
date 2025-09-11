import random

print("Welcome to Rock - Paper - Scissors!")

# Possible choices
choices = ["rock", "paper", "scissors"]
 
while True:
    # Ask user for input
    user_choice = input("Choose Rock, Paper, or Scissors (or type 'q' to quit): ").lower()
    
    # Option to quit the game
    if user_choice == "q":
        print("You quit the game. Goodbye!")
        break
    
    # Check if user input is valid
    if user_choice not in choices:
        print("Invalid choice, please try again.")
        continue
    
    # Computer randomly selects a choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Compare results
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("You lose!")
