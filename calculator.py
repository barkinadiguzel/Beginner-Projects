import math
import statistics
import random

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def average(numbers):
    return statistics.mean(numbers)

def median(numbers):
    return statistics.median(numbers)

def random_number(start, end):
    return random.randint(start, end)

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def calculator():
    print("Welcome to Multi-Tool Calculator!")
    while True:
        print("\nChoose operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Average of numbers")
        print("6. Median of numbers")
        print("7. Generate random number")
        print("8. Celsius to Fahrenheit")
        print("9. Fahrenheit to Celsius")
        print("q. Quit")

        choice = input("Enter your choice: ").lower()

        if choice in ["+", "1", "-", "2", "*", "3", "/", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers.")
                continue

            if choice in ["+", "1"]:
                print("Result:", add(num1, num2))
            elif choice in ["-", "2"]:
                print("Result:", subtract(num1, num2))
            elif choice in ["*", "3"]:
                print("Result:", multiply(num1, num2))
            elif choice in ["/", "4"]:
                print("Result:", divide(num1, num2))

        elif choice in ["5"]:
            nums = input("Enter numbers separated by spaces: ").split()
            nums = [float(n) for n in nums]
            print("Average:", average(nums))

        elif choice in ["6"]:
            nums = input("Enter numbers separated by spaces: ").split()
            nums = [float(n) for n in nums]
            print("Median:", median(nums))

        elif choice in ["7"]:
            try:
                start = int(input("Start of range: "))
                end = int(input("End of range: "))
                print("Random number:", random_number(start, end))
            except ValueError:
                print("Invalid range!")

        elif choice in ["8"]:
            try:
                c = float(input("Enter Celsius: "))
                print("Fahrenheit:", celsius_to_fahrenheit(c))
            except ValueError:
                print("Invalid input!")

        elif choice in ["9"]:
            try:
                f = float(input("Enter Fahrenheit: "))
                print("Celsius:", fahrenheit_to_celsius(f))
            except ValueError:
                print("Invalid input!")

        elif choice == "q":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")

# Run the calculator
calculator()
