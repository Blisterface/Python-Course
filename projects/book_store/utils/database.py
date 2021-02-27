import json


file = open('./library.txt')
books = json.load(file)
file.close()
print(books)

def save():
    save_books = json.dumps(books,indent=4)
    with open('./library.txt','w') as library:
        library.writelines(save_books)

def add_new_book(name,author,read=False):
    book = {"title":name, "author":author, "read":read}
    books.append(book)


def display_books():
    line = "-"*50
    print(line)
    print('{:<20s}{:>10s}{:>15s}'.format('Title','Author','Read'))
    print(line)
    for var in books:
        print('{:<20s}{:>10s}{:>10s}'.format(var['title'],var['author'],str(var['read'])))

"""
def remove_book(title):
    for book in books:
        if book['title'] == title:
            books.remove(book)
            print(f"{title} has been removed from the library")
            return
    print(f"{title} is not in library")
"""
def remove_book(title):
    global books
    books = [book for book in books if book['title']!=title]
    print(f"{title} has been removed from the library")
    



def read_book(title):
    for book in books:
        if book['title'] == title:
            book['read'] = True
            print(f"You have read {title}")
            return
    prompt = input(f"{title} is not in library, would you like to add it? Y/n: ")
    if prompt.capitalize() == 'Y':
        author = input(f"Enter {title} author: ")
        add_new_book(title,author,True)
