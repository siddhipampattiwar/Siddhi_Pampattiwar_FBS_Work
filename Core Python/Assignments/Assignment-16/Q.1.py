# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.

class Book:
    count = 0

    def __init__(self, bid=0, bname="", price=0.0, author=""):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author

        Book.count += 1

    def __del__(self):
        print("Book object deleted")

    def ShowBook(self):
        print("Book Id =", self.bid)
        print("Book Name =", self.bname)
        print("Price =", self.price)
        print("Author =", self.author) 

b1 = Book()
b1.ShowBook()

print()

# Parameterized object
b2 = Book(101, "Python Programming", 500, "James")
b2.ShowBook()

print()

# Another object
b3 = Book(102, "Data Science", 600, "Mark")
b3.ShowBook()

print()

# Display count of objects
print("Total Objects Created =", Book.count)