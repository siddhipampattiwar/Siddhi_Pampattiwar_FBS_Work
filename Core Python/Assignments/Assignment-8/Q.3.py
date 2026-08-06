# Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

#a.
# def sum(n):
#     s = 0
#     for i in range(1, n+1):
#         s = s + i
#     return s

# n = int(input("Enter n: "))
# print(sum(n))

#b.
# def factorial(num):
#     fact=1
#     for i in range(1, num+1):
#         fact=fact*i
#     return fact
# def sum_factorial(n):
#     s=0
#     for i in range(1, n+1):
#         s=s+fact(i)
#     return s

# n=int(input('Enter n: '))
# print(sum_factorial(n))        

#c
def sum_power(n):
    s=0
    for i in range(1,n+1):
        s=s+(i**i)
    return s
n=int(input('Enter n: '))
print('Sum=',sum_power(n))    