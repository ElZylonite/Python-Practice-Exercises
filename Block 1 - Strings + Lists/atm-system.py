balance = 1000
print("""
    1. Balance
    2. Deposit money
    3. Withdraw money
    4. Exit""")


while True:
    action = int(input("> "))
    if action == 1:
        print(f"Balance: {balance}")
    elif action == 2:
        deposit_amount = int(input("How much money would you like to deposit? "))
        if deposit_amount < 0:
            print("You can't deposit negative numbers")
        else:
            balance += deposit_amount
            print(f"Balance: {balance}")

    elif action == 3:
        withdraw_amount = int(input("How much money would you like to withdraw? "))
        if withdraw_amount < 0:
            print("You can't withdraw negative numbers")
        elif withdraw_amount > balance:
            print("Insufficient funds")
        else:
            balance -= withdraw_amount
            print(f"Balance: {balance}")

        

    elif action == 4:
        print("You exited the ATM")
        break
    else:
        print("Invalid input")

