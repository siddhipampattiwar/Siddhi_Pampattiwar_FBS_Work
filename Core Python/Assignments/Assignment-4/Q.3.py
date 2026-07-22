# WAP to print sum of series upto n.
num = int(input("Enter a number: "))

sum = 0

for i in range(1, num + 1):
    sum = sum + i

print("Sum =", sum)

# First: 0 + 1 = 1
# Then: 1 + 2 = 3
# Then: 3 + 3 = 6
# Then: 6 + 4 = 10
# Then: 10 + 5 = 15
