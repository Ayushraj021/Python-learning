class Book:
    def __init__(self, book_id, author, price):
        self.id = book_id
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book ID: {self.id}, Author: {self.author}, Price: ${self.price:.2f}"

# Create 4 Book objects
book1 = Book(1, "J.K. Rowling", 29.99)
book2 = Book(2, "George R.R. Martin", 35.50)
book3 = Book(3, "J.R.R. Tolkien", 25.00)
book4 = Book(4, "Agatha Christie", 19.99)

# Print details of each book
books = [book1, book2, book3, book4]
for book in books:
    print(book)
