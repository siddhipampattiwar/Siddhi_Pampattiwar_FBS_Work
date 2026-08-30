# Python Program to Count the Number of Vowels in a String
s = input("Enter a string: ")

count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print("Number of vowels:", count)