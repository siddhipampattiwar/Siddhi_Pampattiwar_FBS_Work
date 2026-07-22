# WAP to print all numbers in a range divisible by a given number.
# WAP to print all numbers in a range divisible by a given number.

num = int(input("Enter the last number: "))
div = int(input("Enter the divisor: "))

for i in range(1, num + 1):
    if i % div == 0:
        print(i)