import pickle

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def get_contact(self, name):
        return self.contacts.get(name, "Contact not found")
    
    def list_contacts(self):
        return self.contacts
    
    def __str__(self):
        return "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])
    

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main():
    book = load_data()
    while True:
        command = input("Enter command (add, remove, get, list, exit): ").strip().lower()

        if command == "add":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            book.add_contact(name, phone)
            print(f"Contact {name} added.")
        
        elif command == "remove":
            name = input("Entr name: ").strip()
            book.remove_contact(name)
            print(f"Contact {name} removed.")

        elif command == "get":
            name = input("Enter name: ").strip()
            print(book.get_contact(name))

        elif command == "list":
            print("Contacts: ")
            print(book)

        elif command == "exit":
            save_data(book)
            print("Address book saved. Exiting...")
            break

        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
        
