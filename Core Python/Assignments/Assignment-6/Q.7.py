for i in range(1,6):
    for j in range(1,6-i):
        print('  ',end='')
    ch=65

    for j in range(1,i+1):
        print(chr(ch),end=' ')
        ch+=1
    for j in range(1,i):
        print(chr(ch),end=' ') 
        ch+=1
    print()           