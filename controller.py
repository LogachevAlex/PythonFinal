from model import PB
import view

class Controller:
    def __init__(self, filename): #При создании экземпляра контроллера, он инициализирует модель телефонной книги (PB), загружая контакты из файла filename
        self.phonebook = PB(filename)

    def show_all_contacts(self): # запрашивает список всех контактов из модели и передаёт его для отображения. Если контактов нет, выводится соответствующее сообщение.
        if self.phonebook.contacts:
            view.display_contacts(self.phonebook.contacts)
        else:
            view.display_message("Phonebook is empty.")

    def add_contact(self):  # получает данные для нового контакта от пользователя, добавляет контакт в модель и сохраняет обновлённые данные в файл.
        name, number, comment = view.get_contact_input()
        self.phonebook.add_contact(name, number, comment)
        view.display_message("Contact added successfully.")

    def find_contact(self):  # поиск контакта, если контакт не найден, то выдает соответствующее сообщение
        search_term = view.get_search_term()
        found_contacts = self.phonebook.find_contact(search_term)
        if found_contacts:
            view.display_contacts(found_contacts)
        else:
            view.display_message("No contacts found.")

    def update_contact(self): # апдейт контакта, сначала реализуется find_contact, если контакт найдет, то реализуется метод выбора, а потом апдейт контакта
        search_term = view.get_search_term()
        found_contacts = self.phonebook.find_contact(search_term)
        if not found_contacts:
            view.display_message("No contacts found.")
            return

        contact_index = view.choose_contact(found_contacts)
        if contact_index is not None:
            old_name = found_contacts[contact_index].name
            new_name, new_number, new_comment = view.get_contact_input()
            if self.phonebook.update_contact(old_name, new_name, new_number, new_comment):
                view.display_message("Contact updated successfully.")
            else:
                view.display_message("Error updating contact.")

    def delete_contact(self): # удаление контакта, по тому же принципу, что и апдейт
        search_term = view.get_search_term()
        found_contacts = self.phonebook.find_contact(search_term)
        if not found_contacts:
            view.display_message("No contacts found.")
            return

        contact_index = view.choose_contact(found_contacts)
        if contact_index is not None:
            self.phonebook.delete_contact(found_contacts[contact_index].name)
            view.display_message("Contact deleted successfully.")
