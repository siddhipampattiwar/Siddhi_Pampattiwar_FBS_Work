# 2. Create a class Distance with data members as km,m and cm and add following
# methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class Distance:

    # Constructor
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm

    # Destructor
    def __del__(self):
        print("Distance object destroyed")

    # Overload + operator
    def __add__(self, other):
        cm = self.cm + other.cm
        m = self.m + other.m
        km = self.km + other.km

        if cm >= 100:
            m = m + cm // 100
            cm = cm % 100

        if m >= 1000:
            km = km + m // 1000
            m = m % 1000

        return Distance(km, m, cm)

    # Overload - operator
    def __sub__(self, other):
        cm = self.cm - other.cm
        m = self.m - other.m
        km = self.km - other.km

        if cm < 0:
            cm = cm + 100
            m = m - 1

        if m < 0:
            m = m + 1000
            km = km - 1

        return Distance(km, m, cm)

    # Display
    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"


d1 = Distance(5, 200, 50)
d2 = Distance(2, 300, 30)

d3 = d1 + d2
print("Addition =", d3)

d4 = d1 - d2
print("Subtraction =", d4)

