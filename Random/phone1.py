# Improved Phone Contact Manager

contacts = {}

def add_contact():
    name = input("Enter contact name: ").strip().title()
    if name in contacts:
        print(f"Contact '{name}' already exists.")
        return
    phone = input("Enter phone number: ").strip()
    if not phone.isdigit():
        print("Invalid phone number. Please enter only digits.")
        return
    contacts[name] = phone
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Contact List ---")
    for name, phone in sorted(contacts.items()):
        print(f"{name}: {phone}")

def search_contact():
    name = input("Enter the name to search: ").strip().title()
    if name in contacts:
        print(f"Found: {name} - {contacts[name]}")
    else:
        print(f"No contact found with the name '{name}'.")

def delete_contact():
    name = input("Enter the name to delete: ").strip().title()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"No contact found with the name '{name}'.")

def main():
    while True:
        print("\n===== Phone Contact Manager =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
