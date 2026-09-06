class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'"{self.title}" by {self.author}, {self.pages} pages'

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

book1 = Book("Diary of a Wimpy Kid", "Jeff Kinney", 500)
book2 = Book("Diary of a Wimpy Kid", "Jeff Kinney", 500)

print(book1 == book2)