# Python Program to Check if a Given Key Exists in a Dictionary or Not
d = {
    1: "one",
    2: "two",
    3: "three"
}

key = int(input("Enter key: "))

if key in d:
    print("Key exists")
else:
    print("Key does not exist")
