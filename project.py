library = []

def line():
    print("════════════════════════════════════")

def header(title):
    line()
    print(f"          {title}")
    line()

def pause():
    input("\nPress Enter to continue...")

def add_book():
    header("ADD NEW BOOK")

    book_id = input("Enter Book ID: ")

    # 2️⃣ Avoid Duplicate Book IDs
    for b in library:
        if b["id"] == book_id:
            print("\n✘ Book ID already exists! Try a different ID.")
            pause()
            return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    library.append({
        "id": book_id,
        "title": title,
        "author": author
    })

    print("\n✔ Book added successfully!")
    pause()

def view_books():
    header("VIEW ALL BOOKS")

    if not library:
        print("No books available.\n")
    else:
        print("ID\tTitle\t\tAuthor")
        print("----------------------------------------")
        for b in library:
            print(f"{b['id']}\t{b['title']}\t\t{b['author']}")

    pause()

def update_book():
    header("UPDATE BOOK")
    
    book_id = input("Enter Book ID to update: ")

    for b in library:
        if b['id'] == book_id:
            print("\nBook Found!")
            b['title'] = input("Enter new title: ")
            b['author'] = input("Enter new author: ")
            print("\n✔ Book updated successfully!")
            pause()
            return

    print("\n✘ Book not found!")
    pause()

def delete_book():
    header("DELETE BOOK")
    
    book_id = input("Enter Book ID to delete: ")

    for b in library:
        if b['id'] == book_id:
            library.remove(b)
            print("\n✔ Book deleted successfully!")
            pause()
            return

    print("\n✘ Book not found!")
    pause()

def menu():
    while True:
        line()
        print("       📚 LIBRARY BOOK MANAGER")
        line()

        # 🔟 Book Count Display
        print(f"Total Books: {len(library)}")
        print("----------------------------------------")

        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")
        line()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("\nThank you! Exiting program...")
            break
        else:
            print("\nInvalid choice! Try again.")
            pause()

menu()