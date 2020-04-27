def print_menu():
    print("""Choose a number: 
    1. Print all books
    2. Add a book
    3. Delete a book
    4. Update a book
    0. QUIT""")

"""
print("Hello, Welcome to your reading list.")
while(True):
    print_menu()
    response = int(input())
    if response == 1:
        print("Here are all of your books")
    elif response == 2:
        print("adding a book")
    elif response == 3:
        print("Deleting a book")
    elif response == 4:
        print("Updating a book")
    else:
        print("Good luck reading!")
        break
"""

########### CONUMSING SDK ##########


#This brought up some questions on SDK design
#Should deleting/updating a book require book object or just title? ID? So many options
#Not very easy to maintain object as you might easily do with a UI.

import booksSDK
from book import Book

print("Hello, Welcome to your reading list.")
while(True):
    print_menu()
    response = int(input())
    if response == 1:
        print("Here are all of your books:")
        for book in booksSDK.get_books():
            print(book)
    elif response == 2:
        print("Title?")
        title = input()
        print("Pages?")
        pages = input()
        booksSDK.add_book(Book(title, pages))
    elif response == 3:
        print("Title?")
        title = input()
        print("Pages?")
        pages = input()
        booksSDK.delete_book(Book(title, pages))
    elif response == 4:
        print("Current title?")
        current_title = input()
        print("Current pages?")
        current_pages = input()
        print("New title (s for same)")
        new_title = input()
        if str.lower(new_title) == 's':
            new_title = current_title
        print("New pages? (s for same)")
        new_pages = input()
        if str.lower(new_pages) == 's':
            new_pages = current_pages
        booksSDK.update_book(Book(current_title, current_pages), new_title, new_pages)
    else:
        print("Good luck reading!")
        break