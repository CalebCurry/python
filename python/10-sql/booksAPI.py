#execute init.py first to get proper db structure
#delete db and re-run init.py as needed
from book import Book
import sqlite3
import os.path

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
    c.connection.close()


book = Book("Are You My Mother?", 1000)
print("Added book id:", add_book(book))
print("Get book by title:", get_book_by_title(book.title))
print("Not a valid book:", get_book_by_title("yeet"))

add_book(Book('The Digging-est Dog', 76))
print("get books:", get_books())

book = update_book(book, book.title, 76)
print("Updated book:", book)
delete_book(book)
print("After delete:", get_book_by_title("Are You My Mother?"))

print("All books:", get_books())





