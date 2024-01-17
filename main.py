from controller import Controller
import view

def main():
    controller = Controller('contacts.txt')

    while True:
        choice = view.get_user_choice()

        if choice == '1':
            controller.show_all_contacts()
        elif choice == '2':
            controller.add_contact()
        elif choice == '3':
            controller.find_contact()
        elif choice == '4':
            controller.update_contact()
        elif choice == '5':
            controller.delete_contact()
        elif choice == '0':
            break
        else:
            view.display_message("Invalid option, please try again.")

if __name__ == "__main__":
    main()
