# Python Program to count number of digits and letters in a string.
s = input("Enter a string: ")

digits = 0
letters = 0

for ch in s:
    if ch >= '0' and ch <= '9':
        digits += 1
    elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        letters += 1

print("Number of digits:", digits)
print("Number of letters:", letters)