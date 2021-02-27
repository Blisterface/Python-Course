books = []

def add_new_book(name,author):
    book = {"title":name, "author":author, "read":False}
    books.append(book)


def display_books():
    string = "Title \t Author \t Read"
    line = "-"*len(string)
    print(f"{string} \n {line}")
    for var in books:
        print(f"{var['title']} \t {var['author']} \t {var['read']}")


def remove_book(title):
    for book in books:
        if book['title'] == title:
            books.remove(book)
            print(f"{title} has been removed from the library")
            return
    print(f"{title} is not in library")


def read_book(title):
    for book in books:
        if book['title'] == title:
            book['read'] = True
            print(f"You have read {title}")
            return
    prompt = input(f"{title} is not in library, would you like to add it? Y/n: ")
    if prompt.capitalize() == 'Y':
        author = input(f"Enter {title} author: ")
        add_new_book(title,author)
