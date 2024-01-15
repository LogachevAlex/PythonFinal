class ContactView:
    def display_menu(self):
        print("1. Show all contacts")
        print("2. Add a contact")
        print("3. Search for a contact")
        print("4. Update a contact")
        print("5. Delete a contact")
        print("6. Exit")

    def get_choice(self):
        return input("Enter your choice: ")

    def display_contacts(self, contacts):
        for contact in contacts:
            print("Name: {}, Number: {}, Comment: {}".format(*contact))

    def get_contact_info(self):
        name = input("Enter name: ")
        number = input("Enter number: ")
        comment = input("Enter comment: ")
        return name, number, comment

    def get_search_term(self):
        return input("Enter search term: ")

    def show_message(self, message):
        print(message)

    def display_contacts_with_index(self, contacts):
        for index, contact in enumerate(contacts):
            print(f"{index}. Name: {contact[0]}, Number: {contact[1]}, Comment: {contact[2]}")
