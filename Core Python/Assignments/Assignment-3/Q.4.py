# Write a program to input all sides of a triangle and check whether triangle is valid ornot.
a = int(input("Enter first angle = "))
b = int(input("Enter second angle = "))
c = int(input("Enter third angle = "))
if  a+b+c==180 :
    print("It is Valid Triangle")
else:
    print("Invalid")    