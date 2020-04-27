
########## Create a Class and __init__ ##########


#This section is designed to be a simple introduction to object oriented programming
#We are in no way covering everything... 
#Probably will do OOP or intermediate Python series dedicated to this stuff

class Book():
    pass

book = Book()
print(book)

#When we say Book() we are instantiating a new object
#This object iws assigned to the book variable
#Printing it gives us the type and memory location
#You can also get the type:

print(type(book))

#We can check type like so:

if isinstance(book, Book):
    print("It is indeed book. Read it")
else:
    print("nope, not a book")

#We can use the class to make numerous books:
book2 = Book()
#Consider the class as the cookie cutter to make numerous cookies.

#We can add attributes to any object dynamically like so:
book.title = "Goodnight Moon"
print(book.title)

#This is cool and all but every book has a title, so we can make it part of the structure
#This requires a bit more syntax...
#also notice that you can override any class as we go.
class Book():
    def __init__(self, title):
        self.title = title

#consider this the constructor, or the function that is invoked when we create a book.
#self refers to the book being created and we don't have to worry about passing that, it's implicit
#Title is passed in as an argument, and assigned to self.title (the title of the book)
#We will explore this in more detail in a video soon. 

#We then pass a title to the Book as we create it:
book = Book("Goodnight Moon Again")
book2 = Book("Are You My Mother")
print(book.title)
print(book2.title)

#This will now fail as title is required :)
#book3 = Book()  

#If you want the title to be optional you can give it a default (either a value or None):

class Book():
    def __init__(self, title=None):
        self.title = title

book = Book()
print(book.title) #Still exists just no value.

#This fails as .test doesn't exist.
#print(book.test)

#Next up we are going to create methods in our class. 


########## Methods ##########


#A method is just a function on an object.
#We can define any functions to be attached to our objects by putting em in our class
#We just have to have the implicit parameter self

class Book():
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def log(self):
        print(f"{self.title} is {self.pages} pages long")

    def is_short(self):
        if self.pages < 100:
            return true

book = Book("Are You My Mother?", 72)
book.log() #no need to pass anything to self parameter. 

#A note on __init__
#__init__ is also a method, but it's special in that it is invoked automatically
#When we create an object.
#There are a lot of methods with a similar naming structure we are going to see. 
#__eq__, __hash__, __str__, etc. 

if book.is_short():
    #do something
    print("read book")
else:
    print("Aint got time for that")

#Next up I want to explain this self parameter we've been seeing

#Without methods, we would have to create functions like this:

def book_is_short(book):
    if book.pages < 100:
        return true

if book_is_short(book):
    #do something
    print("read book")
else:
    print("Aint got time for that")

#Which would work but not ideal as we'd easily be overwhelemed with so many functions
#And no organization. It's ideally attached to the object as it's related to the object.


########## Class Level Variables ##########


#We're going to talk about class variables.
#Coming from another language, this would be the closest thing to "static" members
#First, we need to understand self.

#self refers to the object things are being invoked on,
#When we create an object. __init__ assigns stuff to self
#That allows each object to have attributes.

#Any time we create a method, we have self as a parameter.
#This means the method is attached to each object.

#if we leave off self, we are creating it at the class level, which is shared for all objects


class Book():
    favs = [] #class

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def log(self):
        print(f"{self.title} is {self.pages} pages long")

    def is_short(self):
        if self.pages < 100:
            return true


book = Book("Are You My Mother?", 72)
book2 = Book("The Digging-est Dog", 72)

Book.favs.append(book)
Book.favs.append(book2)

print(Book.favs) #Favs is related to books, but not tied to one individual book
#We use self as a parameter if it's unique to each object :)


########## __str__ ##########
########## __eq__ ##########
########## __hash__ and Collections ##########


#To save save space we are combing the code for all three of these sections.

class Book():
    favs = [] #class

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def is_short(self):
        if self.pages < 100:
            return true

    #What happens when you pass object to print?
    def __str__(self):
        return f"{self.title}, {self.pages} pages long"

    #What happens when you use ==?
    def __eq__(self, other):
        if(self.title == other.title and self.pages == other.pages):
            return True
    
    #It's approriate to give something for __hash__ when you override __eq__
    # #This is the recommended way if mutable (like it is here):
    __hash__ = None

    #If should immutable, you could do something like this. 
    #This replaces __hash__ = None
    def __hash__(self):
        return hash(self.title) ^ hash(self.pages) #xor with hash of attributes
        #from Mastering Object-Oriented Python

book = Book("Are You My Mother", 72)
print(book)
equal_book = Book("Are You My Mother", 72)
print("Are they considered equal?", book == equal_book) #yep
print("Are they the same object?", book is equal_book) #nope
book2 = Book("The Digging-est Dog", 72)

print(hash(book), hash(book2))

print("old hash", hash(book))
book.title = "new"
print("new hash", hash(book)) #BAD!!! 
#Hashes shouldn't change