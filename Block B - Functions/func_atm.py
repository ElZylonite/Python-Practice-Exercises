def show_menu():
    print("""<------ Welcome! ------>

            1. View balance
            2. Deposit
            3. Withdraw
            4. Exit
          """)

def view_balance(balance):
    print(f"Your balance is ${balance}")
    return balance

def deposit(balance, amount):
    if amount <= 0:
        print("Deposit amount must be greater than zero.")
        return balance
    else:
        balance += amount
        print(f"You have deposited ${amount}. Your new balance is ${balance}.")
        return balance
    

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds.")
        return balance
    elif amount <= 0:
        print("Withdrawal amount must be greater than zero.")
        return balance
    else:
        balance -= amount
        print(f"You have withdrawn ${amount}. Your new balance is ${balance}.")
        return balance

def main():
    balance = 100
    while True:
        show_menu()
        action = int(input("Please select an option (1-4): "))

        if action == 1:
            balance = view_balance(balance)
        elif action == 2:
            amount = float(input("Enter the amount to deposit: "))
            balance = deposit(balance, amount)
        elif action == 3:
            amount = float(input("Enter the amount to withdraw: "))
            balance = withdraw(balance, amount)
        elif action == 4:
            print("Thank you for using our banking system. Goodbye!")
            break 

main()