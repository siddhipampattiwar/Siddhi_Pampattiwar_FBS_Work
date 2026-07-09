#Write a program to reverse three-digit number.
num = 123

a = num // 100
b= (num // 10) % 10
c= num % 10

reverse = c * 100 + b * 10 + a

print("Reverse =", reverse)
