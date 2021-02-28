from .connection_database import DatabaseConnection

database = './data.db'

def create_book_table():
    with DatabaseConnection(database) as conn:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(title text primary key,author text,read integer)')


def add_new_book(title,author,read=False):
    with DatabaseConnection(database) as conn:
        cursor = conn.cursor()
        conn.execute('INSERT INTO books VALUES(?,?,?)',(title,author,read))



def get_books():
    with DatabaseConnection(database) as conn:
        cursor = conn.cursor()
        conn.execute('SELECT * FROM books')
        table = cursor.fetchall()
        books = [{'title':row[0], 'author':row[1], 'read':row[2]} for row in table]
        return books


def read_book(title):
    with DatabaseConnection(database) as conn:
        cursor = conn.cursor()
        conn.execute('UPDATE books SET read = 1 WHERE title = ?',(title,))


def remove_book(title):
    with DatabaseConnection(database) as conn:
        cursor = conn.cursor()
        conn.execute('DELETE FROM books WHERE title=?',(title,))


