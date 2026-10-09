# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

class Product():
    def __init__(self, pid=0,pname="",price=0.0,quantity=0):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity

def __del__(self):
    print("Product object destroyed")

def ShowBook(self):
    print("Product ID=", self.pid) 
    print("Product Name=",self.pname)
    print("Price=", self .price)
    print("Quantity=", self.quantity)       


# Parameterized Constructor
p1 = Product(101, "Laptop", 50000, 2)
p1.ShowBook()

print()

# Parameterless Constructor
p2 = Product()
p2.ShowBook()
