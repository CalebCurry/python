
from book import Book
import sqlite3
import os.path

l = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

conn = sqlite3.connect(os.path.join(l, 'books.db'))

c = conn.cursor()
# Create table
c.execute('''CREATE TABLE IF NOT EXISTS books
             (title TEXT, pages INTEGER)''')

def cursor():
    #https://stackoverflow.com/questions/14511337/efficiency-of-reopening-sqlite-database-after-each-query/14520670
    
    l = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    return sqlite3.connect(os.path.join(l, 'books.db')).cursor()

def add_book(book):
    c = cursor()
    with c.connection:
        c.execute("INSERT INTO books VALUES (?, ?)", (book.title, book.pages))
    c.connection.close() 
    return c.lastrowid

def get_book_by_title(title):
    c = cursor()
    c.execute('SELECT * FROM books WHERE title=?', (title,))
    data = c.fetchone()
    c.connection.close()

    if not data:
        return None

    return Book(data[0], data[1])
        
def get_books():
    c = cursor()
    books = []
    for row in c.execute('SELECT * FROM books'):
        books.append(Book(row[0], row[1]))
    c.connection.close()
    return books

def update_book(book, new_title, new_pages):
    c = cursor()
    with c.connection: #don't forget this part.
        c.execute('UPDATE books SET title=?, pages=? WHERE title=? AND pages=?', 
        (new_title, new_pages, book.title, book.pages))
    book = get_book_by_title(book.title) #after commit
    c.connection.close()
    return book

def delete_book(book):
    c = cursor()
    with c.connection:
        c.execute('DELETE FROM books WHERE title=? AND pages=?', (book.title, book.pages))
    rows = c.rowcount
    c.connection.close()
    return rows