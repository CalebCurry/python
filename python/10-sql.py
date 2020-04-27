########## Intro to SQLite and Creating a Database ##########

import sqlite3 #included with Python

conn = sqlite3.connect(":memory:")

#creating this goes off of the cwd.  CD in terminal changes cwd
#so either cd to correct folder or figure out how to do a more concrete path:
#import os.path
#conn = sqlite3.connect(os.path.realpath('./books.db'))


#we use a cusror object to work with the database 
c = conn.cursor()
#https://stackoverflow.com/questions/6318126/why-do-you-need-to-create-a-cursor-when-querying-a-sqlite-database


########## Create a Table with Python ##########

# Create table
c.execute('''CREATE TABLE books
             (title TEXT, pages INTEGER)''')


########## Insert Data with Python ##########


# Insert a row of data
c.execute("INSERT INTO books VALUES ('Are You My Mother?', 72)")

# Save (commit) the changes
conn.commit()


########## Retrieve Data in Python ##########

c.execute('SELECT * FROM books WHERE title=?', ('Are You My Mother?',))
print(c.fetchone())

books = [
    ('The Digging-est Dog', 72),
    ('Goodnight Moon', 31),
    ('The Giving Tree', 66)
]

c.executemany('INSERT INTO books VALUES (?,?)', books)
conn.commit()

c.execute('SELECT * FROM books')
data = c.fetchall()
print(data)


########## Delete SQLite data in Python ##########

c.execute('SELECT * FROM books WHERE title=?', ('Are You My Mother?',))
print(c.fetchone())
c.execute('DELETE FROM books WHERE title=?', ('Are You My Mother?',)) #don't forget where lol
c.execute('SELECT * FROM books WHERE title=?', ('Are You My Mother?',))
print(c.fetchone())


########## Update SQLite Data in Python ##########

c.execute('SELECT * FROM books WHERE title=?', ('Goodnight Moon',))
print(c.fetchone())
c.execute('UPDATE books SET pages="30" WHERE title="Goodnight Moon"')
c.execute('SELECT * FROM books WHERE title=?', ('Goodnight Moon',))
print(c.fetchone())
conn.commit
c.close()

########## Create an SDK ##########


import booksSDK
from book import Book

book = Book("Are You My Mother?", 1000)
print("Added book id:", booksSDK.add_book(book))
print("Get book by title:", booksSDK.get_book_by_title(book.title))
print("Not a valid book:", booksSDK.get_book_by_title("yeet"))

booksSDK.add_book(Book('The Digging-est Dog', 76))
print("get books:", booksSDK.get_books())

book = booksSDK.update_book(book, book.title, 76)
print("Updated book:", book)
print("Deleted:", booksSDK.delete_book(book))
print("After delete:", booksSDK.get_book_by_title("Are You My Mother?"))

print("All books:", booksSDK.get_books())



