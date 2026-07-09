# WAP to imput two angles from user and find third angle of the triangle.

angle1 = int(input("Enter first angle "))
angle2 = int(input("Enter second angle "))

angle3 = 180 - (angle1 + angle2)

print("Third angle is :", angle3)