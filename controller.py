class ContactController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            self.view.display_menu()
            choice = self.view.get_choice()

            if choice == '1':
                contacts = self.model.read_contacts()
                self.view.display_contacts(contacts)
            elif choice == '2':
                name, number, comment = self.view.get_contact_info()
                self.model.add_contact(name, number, comment)
                self.view.show_message("Contact added successfully.")
            elif choice == '3':
                search_term = self.view.get_search_term()
                found_contacts = self.model.find_contact(search_term)
                self.view.display_contacts(found_contacts)
            elif choice == '4':
                search_term = self.view.get_search_term()
                found_contacts, indices = self.model.find_contact_with_indices(search_term)
                if found_contacts:
                    self.view.display_contacts_with_index(found_contacts)
                    contact_index = int(input("Enter the index of the contact to update: "))
                    if 0 <= contact_index < len(found_contacts):
                        real_index = indices[contact_index]
                        new_name, new_number, new_comment = self.view.get_contact_info()
                        self.model.update_contact_by_index(real_index, new_name, new_number, new_comment)
                        self.view.show_message("Contact updated successfully.")
                    else:
                        self.view.show_message("Invalid index.")
                else:
                    self.view.show_message("No contacts found with the given search term.")
            elif choice == '5':
                name = input("Enter the name of the contact to delete: ")
                self.model.delete_contact(name)
                self.view.show_message("Contact deleted successfully.")
            elif choice == '6':
                break
            else:
                self.view.show_message("Invalid choice, please try again.")