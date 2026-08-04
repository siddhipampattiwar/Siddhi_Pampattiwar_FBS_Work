n = 5

for i in range(-n+1, n):
    for j in range(abs(i), n):
        if j == abs(i) or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()