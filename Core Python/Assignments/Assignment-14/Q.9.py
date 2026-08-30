# Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.
lst = [1, 2, 3, 4, 5]

target = int(input("Enter target: "))

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        for k in range(j + 1, len(lst)):
            if lst[i] + lst[j] + lst[k] == target:
                print(lst[i], lst[j], lst[k])