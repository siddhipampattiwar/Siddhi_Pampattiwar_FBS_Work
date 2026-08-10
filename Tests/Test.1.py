# 1. Write a program to find the area and perimeter of following figure (Accept the length, breadth and radius from user:
import math

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
r = float(input("Enter radius: "))

area = (l * b) + (math.pi * r * r / 2)

perimeter = (2 * l) + b + (math.pi * r)

print("Area =", area)
print("Perimeter =", perimeter) 

# # 2. Write a program to calculate simple interest based on Principal, Rate and Time (SI = P*R*T/100)
p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

si = (p * r * t) / 100

print("Simple Interest =", si)


# # 3. Write a program to accept distance in km and convert it into meters and centimeters both.
km = float(input("Enter distance in km: "))

meter = km * 1000
cm = km * 100000

print("Meter =", meter)
print("Centimeter =", cm)

# #4. Calculate the cost of painting the following building’s walls (both interior and exterior). You need to accept area (one wall) and cost of both interior and
# # exterior wall.
# # (Note: 1. Below diagram is of two joint rooms.
# # 2. It is upper view of building.)
area = float(input("Enter area of wall: "))
inside = float(input("Enter interior cost per sq.ft: "))
outside = float(input("Enter exterior cost per sq.ft: "))

interior_cost = area * inside
exterior_cost = area * outside

total = interior_cost + exterior_cost

print("Interior cost =", interior_cost)
print("Exterior cost =", exterior_cost)
print("Total cost =", total)