# Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)
num = int(input("Enter a number = "))

temp = num #We use temp because the value of num should not change.
count = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** count
    temp = temp // 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")   
