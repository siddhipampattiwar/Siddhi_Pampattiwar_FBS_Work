# Python Program to Concatenate Two Dictionaries Into One
d1 = {"name": "Siddhi", "age": 22}
d2 = {"city": "Amravati", "branch": "AI"}

d = {}

for key in d1:
    d[key] = d1[key]

for key in d2:
    d[key] = d2[key]

print("Combined Dictionary:", d)