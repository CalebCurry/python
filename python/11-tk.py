########## Intro to GUI App Development ##########


#There are numerous "frameworks" you can use to build a user interface with Python
#This is to build desktop applications. 
#Although there may be some debate on which is best, 
#you can probably get the job done with any
#tkinter is build it. So that's what we are going to learn first.

#Seperation between functionality and UI is ideal
#Because of this, we try to keep logic in the UI code minimal
#We can make this easier by creating an SDK to work with the Db (as we did)
#Long term goal is to actually create an API we can consume...
#We'll get into this, but essentially we can have the same backend for:
#   Desktop app
#   CLI
#   Web App
#   Mobile App
#   Etc...

#For now we are going to use the SDK, build out a UI, and then later an API

"""
#Getting started
#Because tkinter is built in, we don't have to download or install anything.
#We just import it:
import tkinter
tk = tkinter.Tk() #This is the start up code just to get a window
#We can modify the window title like so:
tk.title("This is a Title")
tk.mainloop() #This will "start" the application.
print("This will wait")
"""

#Let's build a small application:

from random import randint
import tkinter
from tkinter import messagebox

low = 0
high = 20
rand = randint(low, high)
def check(guess):
    print(guess)
    if guess < rand:
        #tkinter.messagebox.showinfo("No", "You guessed " + str(guess)).pack      
        tkinter.Label(tk, text=f"{guess} is low").pack()
    elif guess > rand:
        tkinter.Label(tk, text=f"{guess} is high").pack()
    else:
        tkinter.messagebox.showinfo("You win!", f"{guess} is correct!")   

tk = tkinter.Tk()
tk.title("Guessing Game")
guess_goal = tkinter.Label(tk, text=f"Guess a number {low} to {high} (inclusive)")
guess_goal.pack()
entry = tkinter.Entry(tk)
entry.pack()
button = tkinter.Button(tk, text="Take a guess", command=lambda: check(int(entry.get())))
button.pack()
tk.mainloop()

########## Tkinter basics ##########
########## Displaying a List of Data with Tkinter ##########
########## Removing List Items in Tkinter ##########
########## Working with SQLlite in Tkinter ##########




"""
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()
"""