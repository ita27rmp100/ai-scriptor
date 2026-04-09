import os
import json

class ContactBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        else:
            return {}

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file)

    def add_contact(self, name, phone, email):
        self.contacts[name] = {'phone': phone, 'email': email}
        self.save_contacts()

    def search_contact(self, name):
        return self.contacts.get(name)

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            return True
        else:
            return False

    def display_contacts(self):
        for name, contact in self.contacts.items():
            print(f'Name: {name}, Phone: {contact["phone"]}, Email: {contact["email"]}')


def main():
    contact_book = ContactBook('contacts.json')
    while True:
        print('\n1. Add Contact')
        print('2. Search Contact')
        print('3. Delete Contact')
        print('4. Display Contacts')
        print('5. Exit')
        choice = input('Choose an option: ')
        if choice == '1':
            name = input('Enter name: ')
            phone = input('Enter phone: ')
            email = input('Enter email: ')
            contact_book.add_contact(name, phone, email)
        elif choice == '2':
            name = input('Enter name: ')
            contact = contact_book.search_contact(name)
            if contact:
                print(f'Phone: {contact["phone"]}, Email: {contact["email"]}')
            else:
                print('Contact not found')
        elif choice == '3':
            name = input('Enter name: ')
            if contact_book.delete_contact(name):
                print('Contact deleted')
            else:
                print('Contact not found')
        elif choice == '4':
            contact_book.display_contacts()
        elif choice == '5':
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
