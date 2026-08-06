# Sum of all prime numbers between 1 to n
def primesum(n):
    s=0
    for i in range(2,n+1):
        prime=True
        for j in range(2,i):
            if i % j==0:
                prime=False
                break
        if prime:
                s=s+i
    return s
n=int(input('Enter n: '))
print('Sum of Prime Numbers =',primesum(n))            