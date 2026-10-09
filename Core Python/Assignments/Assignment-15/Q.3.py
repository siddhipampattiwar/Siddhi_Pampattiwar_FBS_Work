# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook

class Shirt:
    def __init__(self, sid=0 , sname="" , type="" , price=0.0, size=""):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price=price
        self.size=size

    def __del__(self):
        print("Shirt object destroyed")

    def ShowBook(self):
        print("Shirt ID =", self.sid)
        print("Shirt Name =", self.sname)
        print("Type =", self.type)
        print("Price =", self.price)
        print("Size =", self.size)

s1 = Shirt(101, "Peter England", "Formal", 1200, "Large")
s1.ShowBook()

print()

s2 = Shirt()
s2.ShowBook()