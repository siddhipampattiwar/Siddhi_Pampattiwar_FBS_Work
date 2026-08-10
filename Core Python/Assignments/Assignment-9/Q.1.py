# 1. Write a program to find sum of following series using recursive functions:

# i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions
# If n = 4

# 1! + 2! + 3! + 4!

# = 1 + 2 + 6 + 24

# = 33

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


def sum(n):
    if n == 1:
        return 1
    return fact(n) + sum(n-1)


n = int(input("Enter n: "))
print("Sum =", sum(n))