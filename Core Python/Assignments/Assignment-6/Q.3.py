for i in range(0,4):
    num=1

    for j in range(1,4-i+1):
        print('',end=' ')

    for j in range(0,i+1):
        print(num,end=' ')
        num=num*(i-j)//(j+1)

    print()