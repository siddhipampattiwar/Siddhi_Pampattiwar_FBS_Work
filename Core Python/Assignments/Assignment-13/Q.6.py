# Python Program to Multiply All the Items in a Dictionary
n=int(input("Enter a number :"))
d={}

for i in range (n):
    key = input("Enter Key :")
    value = int(input("Enter value :"))
    d[key] = value

product=1
for value in d.values():
    product *= value

print("Product:", product)        
     