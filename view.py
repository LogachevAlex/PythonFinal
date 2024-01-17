def display_contacts(contacts):
    for contact in contacts:
        print(f"Name: {contact.name}, Number: {contact.number}, Comment: {contact.comment}")

def display_message(message):
    print(message)

def get_user_choice():
    print("=" * 22)
    print("Phonebook Application")
    print("=" * 22)
    print()
    print("1. Show all contacts")
    print("2. Add a new contact")
    print("3. Find a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("0. Exit")
    return input("Choose an option: ")

def get_contact_input():
    name = input("Enter name: ")
    number = input("Enter number: ")
    comment = input("Enter comment: ")
    return name, number, comment

def get_search_term():
    return input("Enter search term (name or number): ")

def get_update_input():
    old_name = input("Enter the name of the contact to update: ")
    new_name = input("Enter new name: ")
    new_number = input("Enter new number: ")
    new_comment = input("Enter new comment: ")
    return old_name, new_name, new_number, new_comment

def get_delete_input():
    return input("Enter the name of the contact to delete: ")

def choose_contact(contacts):
    if not contacts:
        print("No contacts to choose from.")
        return None

    print("Choose a contact:")
    for i, contact in enumerate(contacts):
        print(f"{i + 1}. {contact.name}, {contact.number}, {contact.comment}")

    try:
        choice = int(input("Enter the number of the contact (0 to cancel): ")) - 1
        if 0 <= choice < len(contacts):
            return choice
    except ValueError:
        pass
    return None
