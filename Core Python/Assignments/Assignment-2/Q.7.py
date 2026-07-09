#Find the sum of three-digit number.
num = 456

a = num // 100
b = (num // 10) % 10
c = num % 10

sum = a + b + c

print("Sum =", sum)