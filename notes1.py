import json
import datetime
import os

notes = []

def load_notes():
    global notes
    if os.path.exists("notes.json"):
        with open("notes.json", "r", encoding="utf-8") as f:
            notes = json.load(f)

def save_notes():
    with open("notes.json", "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False)

def print_notes():
    for note in notes:
        print("ID: ", note["id"])
        print("Title: ", note["title"])
        print("Body: ", note["body"])
        print("Created: ", note["created"])
        print("Last updated: ", note["last_updated"])
        print()

def add_note():
    title = input("Enter note title: ")
    body = input("Enter note body: ")
    created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    last_updated = created
    note = {"id": len(notes) + 1, "title": title, "body": body, "created": created, "last_updated": last_updated}
    notes.append(note)
    save_notes()
    print("Note added successfully.")

def edit_note():
    id = int(input("Enter note id to edit: "))
    for note in notes:
        if note["id"] == id:
            title = input("Enter new title (press enter to keep existing): ")
            body = input("Enter new body (press enter to keep existing): ")
            if title != "":
                note["title"] = title
            if body != "":
                note["body"] = body
            note["last_updated"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes()
            print("Note edited successfully.")
            return
    print("Note not found.")

def delete_note():
    id = int(input("Enter note id to delete: "))
    for note in notes:
        if note["id"] == id:
            notes.remove(note)
            save_notes()
            print("Note deleted successfully.")
            return
    print("Note not found.")

load_notes()

while True:
    print("Enter a command:")
    print("1: List notes")
    print("2: Add a note")
    print("3: Edit a note")
    print("4: Delete a note")
    print("5: Exit")
    choice = int(input())
    if choice == 1:
        print_notes()
    elif choice == 2:
        add_note()
    elif choice == 3:
        edit_note()
    elif choice == 4:
        delete_note()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")
