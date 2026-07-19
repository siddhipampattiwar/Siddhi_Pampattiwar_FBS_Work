# Write a program to check if given 3 digit number is a palindrome or not.
# A palindrome is a number that reads the same from left to right and right to left.
num = int(input("Enter a 3-digit number = "))

a = num // 100
b = (num // 10) % 10
c = num % 10

reverse = c * 100 + b * 10 + a

if num == reverse:
    print("It is a Palindrome")
else:
    print("It is Not a Palindrome")
