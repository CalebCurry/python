
import tkinter
from book import Book
import booksSDK

tk = tkinter.Tk()
books = []

def add_to_list():

    if title.get() == "" or pages.get() == "":
        return

    book = Book(title.get(), int(pages.get()))
    print(book)
    if(booksSDK.add_book(book)):
        books.append(book)
        lb.insert(tkinter.END, book)
    title.delete(0, tkinter.END)
    pages.delete(0, tkinter.END)

def delete_from_list():
    index_tuple = lb.curselection()
    if booksSDK.delete_book(books.pop(index_tuple[0])):
        lb.delete((index_tuple))

lb = tkinter.Listbox(tk)

for book in booksSDK.get_books():
    books.append(book)
    lb.insert(tkinter.END, book)

lb.pack()

add = tkinter.Button(tk, text="Add Book", command=add_to_list)
add.pack()

delete = tkinter.Button(tk, text="Delete Book", command=delete_from_list)
delete.pack()

tkinter.Label(tk, text="Title:").pack()
title = tkinter.Entry(tk, text="Title to Add:")
title.pack()

tkinter.Label(tk, text="Pages:").pack()
pages = tkinter.Entry(tk, text="Number of pages:")
pages.pack()

tk.mainloop()
