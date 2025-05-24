def show_menu():
    print("\n--- Digital Paper Notepad ---")
    print("1. Write a new note")
    print("2. View saved notes")
    print("3. Exit")

    def write_note():
    note = input("Write your note here: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved successfully!")

def view_notes():
    print("\n--- Your Notes ---")
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if not notes:
                print("No notes yet.")
            else:
                for i, note in enumerate(notes, start=1):
                    print(f"{i}. {note.strip()}")
    except FileNotFoundError:
        print("No notes file found. Start writing your first note!")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            write_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            print("Goodbye! Your notes are saved on digital paper.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


