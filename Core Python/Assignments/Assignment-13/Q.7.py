# Python Program to Remove the Given Key from a Dictionary
n=int(input("Enter number of items :"))
d={}
for i in range(n):
    key = input("Enter Key :")
    value = int(input("Enter Value :"))
    d[key] = value  

key=input("Enter key to remove :")
if key in d:
    del d[key]
    print("key removed")
else:
    print("Key not found")

print("Dictionary :", d)            