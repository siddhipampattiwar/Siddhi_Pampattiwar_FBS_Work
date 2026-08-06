# WAP to check if a given number is Armstrong number or not. For each task create separate functions.
def armstrong(num):
    temp=num
    sum=0

    while temp>0:
        digit=temp%10
        sum=sum+digit*digit*digit 
        temp=temp//10

    if sum==num:
        return True
    else:
        return False

num=int(input('Enter a Number :'))
if armstrong(num):
    print('ArmStrong Number')
else:
    print('Not an ArmStrong Number')        
        