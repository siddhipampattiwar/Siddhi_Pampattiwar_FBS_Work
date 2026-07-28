# WAP to print Armstrong number within a given range
start = int(input("Enter start = "))
end = int(input("Enter end = "))

for num in range(start, end + 1):
    temp = num
    count = len(str(num))
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** count
        temp = temp // 10

    if sum == num:
        print(num)
