class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f"Current balance: ${self.balance}.")

    def deposit(self, amount):
        if amount < 0:
            print("You cannot deposit a negative amount.")
        else:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}.")
    def withdraw(self, amount):
        if amount < 0:
            print("You cannot withdraw a negative amount.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}.")

account = BankAccount("John Doe", 1000)  
while True:
    print("\nWelcome to the Bank Account Management System")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    
    action = input("> ")

    if action == "1":
        account.show_balance()

    elif action == "2":
        amount = float(input("Enter the amount to deposit: "))
        account.deposit(amount)
    elif action == "3":
        amount = float(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
    elif action == "4":
        print("Thank you for using the Bank Account Management System. Goodbye!")
        break