# Write a program to find sum of digits of a number.
num = int(input("Enter a Number: "))

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum of Digits =", sum)