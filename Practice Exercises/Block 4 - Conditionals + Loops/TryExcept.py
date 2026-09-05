while True:
    try:
        number = int(input("Enter a whole number: "))
        print("That is right!")
        break
    except ValueError:
        print("That is not a number!")
        print("Try again!")
