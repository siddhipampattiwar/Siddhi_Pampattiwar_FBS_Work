# Write a program to reverse a number using recursion.
def reverse(num, rev=0):
    if num == 0:
        return rev

    rem = num % 10
    rev = rev * 10 + rem

    return reverse(num // 10, rev)


num = int(input("Enter a number: "))

print("Reverse:", reverse(num))