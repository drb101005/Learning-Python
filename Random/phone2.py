import json
import os

class Contact:
    def __init__(self, name, phone):
        self.name = name.title()
        self.phone = phone

    def to_dict(self):
        return {"name": self.name, "phone": self.phone}

class PhoneBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return {contact["name"]: contact["phone"] for contact in json.load(f)}
        return {}

    def save_contacts(self):
        with open(self.filename, 'w') as f:
            json.dump([{"name": name, "phone": phone} for name, phone in self.contacts.items()], f, indent=4)

    def add_contact(self, name, phone):
        name = name.title()
        if name in self.contacts:
            print(f"❗ Contact '{name}' already exists.")
        else:
            self.contacts[name] = phone
            self.save_contacts()
            print(f"✅ Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("📭 No contacts found.")
        else:
            print("\n--- 📒 Contact List ---")
            for name, phone in sorted(self.contacts.items()):
                print(f"{name}: {phone}")

    def search_contact(self, name):
        name = name.title()
        if name in self.contacts:
            print(f"🔍 Found: {name} - {self.contacts[name]}")
        else:
            print(f"❌ No contact found with the name '{name}'.")

    def delete_contact(self, name):
        name = name.title()
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"🗑️ Contact '{name}' deleted.")
        else:
            print(f"❌ No contact found with the name '{name}'.")

def main():
    phonebook = PhoneBook()

    while True:
        print("\n📱 PHONE CONTACT MANAGER 📱")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            if not phone.isdigit():
                print("⚠️ Phone number must contain only digits.")
            else:
                phonebook.add_contact(name, phone)

        elif choice == '2':
            phonebook.view_contacts()

        elif choice == '3':
            name = input("Enter name to search: ").strip()
            phonebook.search_contact(name)

        elif choice == '4':
            name = input("Enter name to delete: ").strip()
            phonebook.delete_contact(name)

        elif choice == '5':
            print("👋 Exiting Phone Contact Manager.")
            break
        else:
            print("⚠️ Invalid choice. Enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
