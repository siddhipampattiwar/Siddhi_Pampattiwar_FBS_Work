# WAP to print all odd numbers until n.
num = int(input("Enter a number: "))

for i in range(1, num + 1, 2):
    print(i)
    
# We start from 1 because 1 is the first odd number.
# Odd numbers are:
# 1, 3, 5, 7, 9, 11...