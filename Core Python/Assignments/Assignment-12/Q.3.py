# Python Program to Detect if Two Strings are Anagrams
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) == len(s2) and sorted(s1) == sorted(s2):
    print("Strings are Anagrams")
else:
    print("Strings are not Anagrams")