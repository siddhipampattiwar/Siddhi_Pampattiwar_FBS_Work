#1. Write a program to print first n prime numbers
n = int(input("Enter n: "))

count = 0
num = 2

while count < n:
    flag = 0

    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break

    if flag == 0:
        print(num, end=" ")
        count += 1

    num += 1

#2.Write a program to calculate the sum of following series where n is input by user. 1/1! + 2/2! + 3/3! + 4/4! + ... N/N!
n = int(input("Enter n: "))

sum = 0
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (i / fact)

print("Sum =", sum)

#3.Write a program to accept basic salary of n emp. (n should be accepted from user). If basic salary is below 20000 then da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and hra=20%. Based on this calculate the total salary of each emp and also total salary of all emp.
n = int(input("Enter number of employees: "))

total_salary = 0

for i in range(1, n + 1):

    basic = float(input("Enter basic salary: "))

    if basic < 20000:
        da = basic * 10 / 100
        ta = basic * 12 / 100
        hra = basic * 15 / 100
    else:
        da = basic * 15 / 100
        ta = basic * 18 / 100
        hra = basic * 20 / 100

    salary = basic + da + ta + hra

    print("Total salary =", salary)

    total_salary = total_salary + salary

print("Total salary of all employees =", total_salary)

#4. Write a program to print pattern 10101 01010 10101 01010 10101
for i in range(5):
    for j in range(5):

        if (i + j) % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")

    print()