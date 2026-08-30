# Python Program to Take in a String and Replace Every Blank Space  with Hyphen
s = input("Enter a string: ")

new_string = ""

for ch in s:
    if ch == " ":
        new_string += "-"
    else:
        new_string += ch

print(new_string)