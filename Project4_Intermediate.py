# Mobile_Contacts

Contacts = {}

def add_contact():
    name = input("Enter name :")
    phone_number = int(input("Enter Phone Number :"))
    Contacts[name] = phone_number
    print("Contact is added succesfully")

def view_contact():
    if not Contacts:
        print("Sorry,Contact not found")
    else:
        for name,phone_number in Contacts.items():
            print(f"{name} : {phone_number}")

def search_contact():
    Search_name = input("Search name : ")
    if Search_name in Contacts:
        print(f"{Search_name} : {Contacts[Search_name]}")
    else:
        print("Contact is not found")

def delete_contact():
    delete = input("Enter the name to delete: ")
    if delete in Contacts:
        del Contacts[delete]
        print(f"{delete} is succesfully deleted")
    else:
        print(f"{delete} is not in your contact")

while True:
    print(".......MOBILE CONTACTS........")
    print("1: Add Contacts")
    print("2: View Contact")
    print("3: Search Contact")
    print("4: Delete Contact")
    print("5: Exit")

    Choice = input("Enter your choice :")

    if Choice == '1':
        add_contact()
    elif Choice == '2':
        view_contact()
    elif Choice == '3':
        search_contact()
    elif Choice == '4':
        delete_contact()
    elif Choice == '5':
        print("Thank you, Have a great day, Bye!")
        break
    else:
        print("Invalid Choice")

    





