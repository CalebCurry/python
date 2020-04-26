import sqlite3
import os.path

#Why are paths so complicated?
#https://stackoverflow.com/questions/4060221/how-to-reliably-open-a-file-in-the-same-directory-as-a-python-script

l = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

conn = sqlite3.connect(os.path.join(l, 'books.db'))

c = conn.cursor()
# Create table
c.execute('''CREATE TABLE books
             (title TEXT, pages INTEGER)''')

#Any seed data
