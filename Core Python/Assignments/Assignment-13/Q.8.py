# Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary
s = input("Enter a string: ")

words = s.split()

d = {}

for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(d)