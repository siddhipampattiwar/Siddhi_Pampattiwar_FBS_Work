# Write a program to check if given number is Armstrong or not using recursive function.
def armstrong(n, digits):
    if n == 0:
        return 0
    return (n % 10) ** digits + armstrong(n // 10, digits)


num = int(input("Enter number: "))

digits = len(str(num))

if armstrong(num, digits) == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")