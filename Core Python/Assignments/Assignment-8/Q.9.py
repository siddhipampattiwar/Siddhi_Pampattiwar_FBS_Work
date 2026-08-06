# Write a program to check if entered number is a palindrome or not.
num = int(input("Enter a Number: "))

temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if num == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")