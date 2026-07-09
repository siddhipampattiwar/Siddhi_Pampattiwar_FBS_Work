# Write a program to enter P, T, R and calculate Compound Interest.
# Amount = p * (1 + r / 100 ) ** t
# Compound Interest = amount - principle


principle = int(input("Principle Amount :"))
time = int(input("Time :"))
rate = int(input("Enter Rate :"))

amount = principle *(1 + rate / 100)**time

Compound_Interest = amount - principle

print (f"Compound_Interest is :, {Compound_Interest}, Amount is : {amount} ")