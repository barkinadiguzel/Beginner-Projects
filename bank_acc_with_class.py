class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}$ deposited. New balance: {self.balance}$")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount}$ withdrawn. New balance: {self.balance}$")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}$")
 
# Main program
name = input("Enter account owner name: ")
account = BankAccount(name)

while True:
    print("\nOptions: 1. Deposit  2. Withdraw  3. Show Balance  4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
