class Book():
    favs = []

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def is_short(self):
        return self.pages < 100

    def __str__(self):
        return f"{self.title}, {self.pages} pages long"

    def __eq__(self, other):
        return self.title == other.title and self.pages == other.pages
            
    
    __hash__ = None

    def __repr__(self): #added to make list of items invoke str
        return self.__str__()
