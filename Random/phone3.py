import json
import os
from typing import Dict

class Contact:
    def __init__(self, name: str, phone: str):
        self.name = name.title()
        self.phone = phone

    def to_dict(self) -> Dict[str, str]:
        return {"name": self.name, "phone": self.phone}




class PhoneBook:
    def __init__(self, filename: str = 'contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self) -> Dict[str, str]:
        """Load contacts from a JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    return {contact["name"]: contact["phone"] for contact in data}
            except (json.JSONDecodeError, KeyError):
                print("⚠️ Failed to load contacts. File may be corrupted.")
        return {}



    def save_contacts(self) -> None:
        """Save contacts to a JSON file."""
        with open(self.filename, 'w') as f:
            json.dump(
                [Contact(name, phone).to_dict() for name, phone in self.contacts.items()],
                f,
                indent=4
            )

    def add_contact(self, name: str, phone: str) -> None:
        name = name.title()
        if name in self.contacts:
            print(f"❗ Contact '{name}' already exists.")
        else:
            self.contacts[name] = phone
            self.save_contacts()
            print(f"✅ Contact '{name}' added.")

    def view_contacts(self) -> None:
        if not self.contacts:
            print("📭 No contacts found.")
        else:
            print("\n--- 📒 Contact List ---")
            for name, phone in sorted(self.contacts.items()):
                print(f"{name}: {phone}")

    def search_contact(self, name: str) -> None:
        name = name.title()
        if name in self.contacts:
            print(f"🔍 Found: {name} - {self.contacts[name]}")
        else:
            print(f"❌ No contact found with the name '{name}'.")

    def delete_contact(self, name: str) -> None:
        name = name.title()
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"🗑️ Contact '{name}' deleted.")
        else:
            print(f"❌ No contact found with the name '{name}'.")

def get_valid_phone() -> str:
    while True:
        phone = input("Enter phone number: ").strip()
        if phone.isdigit():
            return phone
        print("⚠️ Phone number must contain only digits.")

def main():
    phonebook = PhoneBook()

    menu_options = {
        '1': 'Add Contact',
        '2': 'View Contacts',
        '3': 'Search Contact',
        '4': 'Delete Contact',
        '5': 'Exit'
    }

    while True:
        print("\n📱 PHONE CONTACT MANAGER 📱")
        for key, value in menu_options.items():
            print(f"{key}. {value}")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            name = input("Enter name: ").strip()
            phone = get_valid_phone()
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
