class Library:
    def __init__(self):
    self.books = []

# ----------->

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
# ------------>

class Author:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name