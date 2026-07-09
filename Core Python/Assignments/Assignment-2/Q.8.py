#Write a program to swap two numbers using third variable.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a # → Store the value of a in a third variable (temp).
a=b
b=temp

print ("After swapping:")
print("a =", a)
print("b =", b)

#OR

a = 10
b = 20

temp = a
a = b
b = temp

print("a =", a)
print("b =", b)