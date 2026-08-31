# 1er Mini Ejercicio
user_name = ("Enter your username: ")
valid = True
for i in user_name:
    if i.isdigit():
        print("Your username must not contain digits")
        valid = False
        if valid == False:
            break
    elif i.isupper():
        print("Your username must not be uppercase")
        valid = False
        if valid == False:
            break
if valid:
    print(user_name)
