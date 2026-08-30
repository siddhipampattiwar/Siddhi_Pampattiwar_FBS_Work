# Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.
lst = [2,4,6,8,10]
n=int(input("Enter sum value: "))

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i]+lst[j] == n:
            print(lst[i], lst[j])
