# Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

missing_in_B = A - B
missing_in_A = B - A

print("Missing in second set:", missing_in_B)
print("Missing in first set:", missing_in_A)