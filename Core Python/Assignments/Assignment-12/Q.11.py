# Python Program to replace every blank space with hyphen in a string.
s=input("Enter a String:")
new_string = " "

for ch in s:
    if ch == " ":
        new_string += "-"
    else:
        new_string += ch
print(new_string)           


