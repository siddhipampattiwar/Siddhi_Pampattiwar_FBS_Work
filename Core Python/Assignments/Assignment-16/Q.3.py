# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.

class Shirt:

    # Constructor
    def __init__(self, sid=0, sname="", type="", price=0.0, size=""):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    # Destructor
    def __del__(self):
        print("Shirt object deleted")

    # Static method
    @staticmethod
    def calculatePrice(price, size):
        if size.lower() == "small":
            return price
        elif size.lower() == "medium":
            return price + (price * 10 / 100)
        elif size.lower() == "large":
            return price + (price * 20 / 100)
        elif size.lower() == "xlarge":
            return price + (price * 30 / 100)
        else:
            return price

    # ShowBook
    def ShowBook(self):
        finalPrice = Shirt.calculatePrice(self.price, self.size)

        print("Shirt Id =", self.sid)
        print("Shirt Name =", self.sname)
        print("Type =", self.type)
        print("Size =", self.size)
        print("Price =", finalPrice)


# Parameterless object
s1 = Shirt()
s1.ShowBook()

print()

# Parameterized objects
s2 = Shirt(101, "Peter England", "Formal", 1000, "Small")
s2.ShowBook()

print()

s3 = Shirt(102, "Raymond", "Formal", 1000, "Medium")
s3.ShowBook()

print()

s4 = Shirt(103, "Louis Philippe", "Formal", 1000, "Large")
s4.ShowBook()

print()

s5 = Shirt(104, "Allen Solly", "Casual", 1000, "Xlarge")
s5.ShowBook()


