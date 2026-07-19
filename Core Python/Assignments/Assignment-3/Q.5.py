# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
# Equilateral Triangle → All three sides are equal.
# Isosceles Triangle → Any two sides are equal.
# Scalene Triangle → All three sides are different.
# Write a program to check whether the triangle is
# Equilateral, Isosceles or Scalene Triangle.

a = int(input("Enter first side of triangle = "))
b = int(input("Enter second side of triangle = "))
c = int(input("Enter third side of triangle = "))

if a == b and b == c:
    print("The triangle is Equilateral Triangle")
elif a == b or b == c or a == c:
    print("The triangle is Isosceles Triangle")
else:
    print("The triangle is Scalene Triangle")   