# WAP to check if given number is Perfect Number.
# 6 → Factors: 1, 2, 3
# 1 + 2 + 3 = 6 
num = int(input('Enter a number = '))
sum=0

for i in range(1, num):
    if num%i==0:
        sum=sum+i

if sum == num:
    print('Perfect Number')

else:
    print('Not Perfect Number')    




