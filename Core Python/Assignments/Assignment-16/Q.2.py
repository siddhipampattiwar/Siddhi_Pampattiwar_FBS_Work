# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.
class Book:
    count = 0

    def __init__(self, bid=0,bname="",price = 0.0, author = ""):
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

b2 = Book(101,"Python Programming", 500, "Siddhi")
b2.ShowBook()

print()

b3=Book(102,"Data Science", 600, "Mark")
b3.ShowBook()

print()

print("Total Objects Created=", Book.count)