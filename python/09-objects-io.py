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
    

########## Passing by Object Reference ##########


book = Book("Where Is My Mother?", 100)
print(book)

def modify(book): 
    book.title = "Changed noob"

modify(book)
print(book)

#What is we print id to follow? 

def modify(book): 
    print(id(book))
    book.title = "Changed noob"
    print(id(book))

print(id(book))
modify(book)
print(id(book))

#We get the same number for everything

book = Book("Are You My Mother?", 100)
print("let's reassign")
def modify(book): 
    print(id(book))
    book = Book("Changed noob", 100)
    print(id(book)) #This is a different id. 
    #The original is unchanged. Reassigning

print(id(book))
modify(book)
print(id(book))
print(book) #Stayed the same!


########## Reading from a file ##########
########## Context manager (as?) ##########
########## Intro to Exception handling ##########