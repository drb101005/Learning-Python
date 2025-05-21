# Simple Phone Contact Manager

# Dictionary to store contacts
contacts = {}

def add_contact(name, phone_number):
    contacts[name] = phone_number
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Your Contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")

def main():
    while True:
        print("\n--- Phone Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            add_contact(name, phone_number)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            print("Exiting Phone Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
