contacts = {
    "Ana": {"age": 25, "city": "Madrid"},
    "Luis": {"age": 30, "city": "Sevilla"}
}


while True:
    print("What would you like to do?")
    print("""
        1 - Search contact
        2 - Add contact
        3 - View all contacts
        4 - Update contact
        5 - Exit
        """)
    action = int(input("> "))

    if action == 1:
        contact_name = input("Enter contact name: ")
        if contact_name in contacts:
            print(contacts[contact_name])
        else:
            print("No contact found with that name")

    elif action == 2:
        contact_name = input("Enter contact name: ")
        if contact_name not in contacts:
            new_age = int(input("Enter age: "))
            new_city = input("Enter city: ")
            contacts[contact_name] = {"age": new_age, "city": new_city}
            print("Contact added")
        else:
            print("A contact with that name already exists")

    elif action == 3:
        print(contacts)

    elif action == 4:
        contact_name = input("Enter contact name: ")
        if contact_name in contacts:
            field = input("What would you like to update? (age/city): ")
            if "age" in field:
                new_age = int(input("Enter new age: "))
                contacts[contact_name]["age"] = new_age
                print("Age updated")
            elif "city" in field:
                new_city = input("Enter new city: ")
                contacts[contact_name]["city"] = new_city
                print("City updated")
            else:
                print("Please select a valid option (age or city)")
        else:
            print("No contact found with that name")

    elif action == 5:
        break