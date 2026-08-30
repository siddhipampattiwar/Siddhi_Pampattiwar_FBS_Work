# Python Program to count number of lowercase characters in a string.
s = input("Enter a string: ")

count = 0

for ch in s:
    if ch >= 'a' and ch <= 'z':
        count += 1

print("Number of lowercase characters:", count)
