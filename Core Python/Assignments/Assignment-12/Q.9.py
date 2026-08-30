# Python Program to Calculate the Number of Words and the Number of Characters Present in a String
s = input("Enter a string: ")

words = 0
characters = 0

for ch in s:
    characters += 1

    if ch == " ":
        words += 1

words += 1

print("Number of words:", words)
print("Number of characters:", characters)