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
    author = input(f"Enter {title} author")
    database.add_new_book(title,author)


def list_books():
    database.display_books()


def mark_read():
    title = input("Enter book title: ")
    database.read_book(title)


def delete_book():
    title = input("Enter book to delete: ")
    database.remove_book(title)


action = {'a':add_book, 'l':list_books, 'r':mark_read, 'd':delete_book}

def menu():
    user_input = input(choice)
    while user_input != 'q':
        operation = action[user_input]
        operation()
        user_input = input(choice)
def main():
    menu()


if __name__== '__main__':
    main()
