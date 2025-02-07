class Book:
    def __init__(self, title=None, author=None, isbn=0, price=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("ISBN:", self.isbn)
        print("Price:$", self.price)
        print("-" * 30)
    def expensive(self, limit=30):
        return self.price > limit