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

