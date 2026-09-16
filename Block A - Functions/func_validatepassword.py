def validate_password(password):
    """
    Validate the strength of a password.

    A strong password should:
    - Be at least 8 characters long
    - Contain both uppercase and lowercase letters
    - Include at least one numerical digit
    - Have at least one special character (e.g., !, @, #, $)
    """
    requirements = {
        "Minimum Length": False,
        "Uppercase Letters": False,
        "Lowercase Letters": False,
        "Numerical Digits": False,
        "Special Characters": False
    }
    valid = False
    errors = []

    if len(password) >= 8:
        requirements["Minimum Length"] = True
        for i in password:
            if i.isupper():
                requirements["Uppercase Letters"] = True
            if i.islower():
                requirements["Lowercase Letters"] = True
            if i.isdigit():
                requirements["Numerical Digits"] = True
            if not i.isalpha() and not i.isdigit():
                requirements["Special Characters"] = True
    if all(requirements.values()):
        valid = True
        
    elif not valid:
        for i in requirements:
            if requirements[i] == False:
                errors.append(f"- {i} ❌")
    return valid, errors


print(validate_password("Ab2!"))          

    