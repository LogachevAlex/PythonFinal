class ContactModel:
    def __init__(self, filename):
        self.filename = filename

    def read_contacts(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                return [line.strip().split(';') for line in file]
        except FileNotFoundError:
            return []

    def write_contacts(self, contacts):
        with open(self.filename, 'w',  encoding='utf-8') as file:
            for contact in contacts:
                file.write(';'.join(contact) + '\n')

    def add_contact(self, name, number, comment):
        contacts = self.read_contacts()
        contacts.append([name, number, comment])
        self.write_contacts(contacts)

    def find_contact(self, search_term):
        contacts = self.read_contacts()
        return [c for c in contacts if search_term in c[0] or search_term in c[1]]

    # def update_contact(self, selected_name, new_name, new_number, new_comment):
    #     contacts = self.read_contacts()
    #     found = False
    #     for i, contact in enumerate(contacts):
    #         if selected_name.lower() in contact[0].lower():
    #             contacts[i] = [new_name, new_number, new_comment]
    #             found = True
    #             break
    #     if found:
    #         self.write_contacts(contacts)
    #         return True
    #     else:
    #         return False
        
    def find_contact_with_indices(self, search_term):
        contacts = self.read_contacts()
        found_contacts = []
        indices = []
        for i, contact in enumerate(contacts):
            if search_term.lower() in contact[0].lower() or search_term.lower() in contact[1]:
                found_contacts.append(contact)
                indices.append(i)
        return found_contacts, indices


    def update_contact_by_index(self, index, new_name, new_number, new_comment):
        contacts = self.read_contacts()
        if 0 <= index < len(contacts):
            contacts[index] = [new_name, new_number, new_comment]
            self.write_contacts(contacts)
            return True
        else:
            return False

    def delete_contact(self, name):
        contacts = self.read_contacts()
        contacts = [c for c in contacts if c[0] != name]
        self.write_contacts(contacts)
