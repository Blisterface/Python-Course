import sqlite3
import json

file = './library.json'

library = open(file,'r')
books = json.load(library)
library.close()
print(books)

def save():
    save_books = json.dumps(books,indent=4)
    with open(file,'w') as f:
        f.writelines(save_books)

def add_new_book(name,author,read=False):
    book = {"title":name, "author":author, "read":read}
    with open(file,'a') as library:
        library.write(f'{book}\n')

def get_books():
    with open(file,'r') as library:
        return json.load(library)


def display_books():
    line = "-"*75
    print(line)
    print('{:<30s}{:<30s}{:<10s}'.format('Title','Author','Read'))
    print(line)
    book_list = get_books()
    for var in book_list:
        print('{:<30s}{:<30s}{:<10s}'.format(var['title'],var['author'],str(var['read'])))

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
