import random

def dice_roller():
    print("Welcome to the Dice Roller!")
    while True:
        try:
            num_dice = int(input("How many dice do you want to roll? "))
            if num_dice <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        rolls = [random.randint(1, 6) for _ in range(num_dice)]
        print("You rolled:", rolls)
        print("Total:", sum(rolls))

        again = input("Roll again? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break

# Run the dice roller
dice_roller()
