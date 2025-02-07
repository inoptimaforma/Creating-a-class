if __name__ == "__main__":
    books = []
    num_books = int(input("How many books do you need? "))
    for i in range(num_books):
        print("Enter the book's details:", i + 1)
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        price = float(input("Price: $"))
        book = Book(title, author, isbn, price)
        books.append(book)
    print("Book's details:")
    for book in books:
        book.display_info()
        if book.expensive():
            print("The book is expensive.")
        else:
            print("The book is affordable.")
        print("-" * 30)
