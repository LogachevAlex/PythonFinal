11
from model import ContactModel
from view import ContactView
from controller import ContactController

def main():
    model = ContactModel("contacts.txt")
    view = ContactView()
    controller = ContactController(model, view)
    controller.run()

if __name__ == "__main__":
    main()
