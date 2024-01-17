class Contact:
    def __init__(self, name, number, comment):
        self.name = name
        self.number = number
        self.comment = comment

    def __str__(self):
        return f"{self.name};{self.number};{self.comment}"


class PB:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        contacts = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    name, number, comment = line.strip().split(';')
                    contacts.append(Contact(name, number, comment))
        except FileNotFoundError:
            pass  # File not found, starting with an empty phonebook
        return contacts

    def save_contacts(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            for contact in self.contacts:
                file.write(str(contact) + '\n')

    def add_contact(self, name, number, comment):
        self.contacts.append(Contact(name, number, comment))
        self.save_contacts()

    def find_contact(self, search_term):
        return [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or 
                search_term in contact.number]

    def update_contact(self, old_name, new_name, new_number, new_comment):
        for contact in self.contacts:
            if contact.name == old_name:
                contact.name = new_name
                contact.number = new_number
                contact.comment = new_comment
                self.save_contacts()
                return True
        return False

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]
        self.save_contacts()
