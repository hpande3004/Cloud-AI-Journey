'''Practice Code'''
class Book:
    def __init__(self, title,author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

    def __len__(self):
        return self.pages

book = Book("\"Diary of a Wimpy Kid\"", "Jeff Kinney", 500)
print(book)
print(len(book))