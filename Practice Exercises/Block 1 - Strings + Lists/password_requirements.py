password_length = False
upper = False
numeric = False
special = False
valid = False

while not valid:
    password_length = False
    upper = False
    numeric = False
    special = False
    valid = False
    print("----REQUIREMENTS----")
    requirements = """
    - Minimum Length: 8 characters
    - At least one capital letter
    - At least one numeric character
    - At least one special character
    """
    print(requirements)
    password = input("Insert new password: ")
    if len(password) >= 8:
        password_length = True
        print("- Minimum Length: 8 characters ✅")
        for i in password:
            if i.isupper() and not upper:
                print("- At least one uppercase letter ✅")
                upper = True

            elif i.isdigit() and not numeric:
                print("- At least one numeric character ✅")
                numeric = True

            elif not i.isalpha() and not i.isdigit() and not special:
                print("- At least one special character ✅")
                special = True
        if upper and numeric and special:
            valid = True
        else:
            print("Your password has not met all the requirements, try again")
    else:
        print("Your password has not met all the requirements, try again")

else:
    print("Your password met all the requirements")



