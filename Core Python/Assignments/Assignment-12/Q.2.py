# Python Program to Remove the nth Index Character from a Non-Empty String
s = input("Enter a string: ")
n = int(input("Enter index to remove: "))

new_string = s[:n] + s[n+1:]

print("String after removing character:", new_string)