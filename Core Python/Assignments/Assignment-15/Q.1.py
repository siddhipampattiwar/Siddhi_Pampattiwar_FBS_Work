# Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
class Book:
    def __init__(self, bid=0 , bname="", price=0.0 , author=""):
        self.bid=bid
        self.bname=bname
        self.price=price
        self.author=author

    def __del__(self):
        print("Book object destroyed")

    def ShowBook(self):
        print("Book ID=",self.bid)
        print("Book Name=",self.bname)
        print("Price=", self.price) 
        print("Author=",self.author)      

b1 = Book(101,"Data Science" , 500 , "Siddhi")

b1.ShowBook()

print()

b2=Book()

b2.ShowBook()