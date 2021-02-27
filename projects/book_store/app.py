from utils import database

choice = """
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
"""

def add_book():
    title = input("Enter book title: ")
    author = input(f"Enter {title} author: ")
    database.add_new_book(title,author)


def list_books():
    database.display_books()


def mark_read():
    title = input("Enter book title: ")
    database.read_book(title)


def delete_book():
    title = input("Enter book to delete: ")
    database.remove_book(title)


def exit_app():
    quit = input("Save library before exiting application (Y/n): ")
    if quit.capitalize() == 'Y':
        database.save()
    

action = {'a':add_book, 'l':list_books, 'r':mark_read, 'd':delete_book,'q':exit_app}

def menu():
    while True:
        user_input = input(choice)
        try:
            operation = action[user_input]
            if operation == exit_app:
                operation()
                break
            operation()
        except KeyError:
            print("Choose valid operation from given the menu...")


def main():
    menu()


if __name__== '__main__':
    main()
