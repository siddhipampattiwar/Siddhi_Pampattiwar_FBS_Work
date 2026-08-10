# Write a program to reverse a given number using recursive function.
def reverse(n, rev=0):
    if n == 0:
        return rev
    return reverse(n // 10, rev * 10 + n % 10)


num = int(input("Enter number: "))

print("Reverse =", reverse(num))