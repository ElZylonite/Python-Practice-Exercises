def is_long(password):
    if len(password) >= 8:
        return True
    else:
        return False

def has_uppercase(password):
    for c in password:
        if c.isupper():
            return True
    return False

def has_lowercase(password):
    for c in password:
        if c.islower():
            return True
    return False

def has_digit(password):
    for c in password:
        if c.isdigit():
            return True
    return False
def has_special_char(password):
    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    for c in password:
        if c in special_chars:
            return True
    return False

def is_valid(password):
    return (is_long(password) and has_uppercase(password) and has_lowercase(password) and has_digit(password) and has_special_char(password))

while True:
    password = input("Enter your password: ")
    long_enough = is_long(password)
    uppercase = has_uppercase(password)
    lowercase = has_lowercase(password)
    digit = has_digit(password)
    special = has_special_char(password)

    if long_enough and uppercase and lowercase and digit and special:
        print("Password is valid.")
        break
    elif not long_enough:
        print("Password must be at least 8 characters long.")
    elif not uppercase:
        print("Password must contain at least one uppercase letter.")
    elif not lowercase:
        print("Password must contain at least one lowercase letter.") 
    elif not digit:
        print("Password must contain at least one digit.")
    elif not special:
        print("Password must contain at least one special character.")