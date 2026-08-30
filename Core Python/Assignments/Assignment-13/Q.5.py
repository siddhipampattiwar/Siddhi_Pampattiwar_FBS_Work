# Python Program to Sum All the Items in a Dictionary
n=int(input("Enter a number :"))
d={}
for i in range (n):
    key = input("Enter key :")
    value = int(input("Enter value :"))
    d[key] = value

total = 0

for value in d.values():
    total += value

print("Sum:", total)    
