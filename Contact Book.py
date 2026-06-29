contacts = {}

while True:

    print("\n1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. View Contacts")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        contacts[name] = phone

        print("Contact Added Successfully")

    elif choice == 2:

        name = input("Enter Contact Name: ")

        if name in contacts:
            phone = input("Enter New Number: ")
            contacts[name] = phone
            print("Updated Successfully")
        else:
            print("Contact Not Found")

    elif choice == 3:

        name = input("Enter Contact Name: ")

        if name in contacts:
            del contacts[name]
            print("Deleted Successfully")
        else:
            print("Contact Not Found")

    elif choice == 4:

        print("\nContacts")
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == 5:
        break

    else:
        print("Invalid Choice")