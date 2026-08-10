# Python Program to Sort a List According to the Length of the Elements within the list.
li = ["apple", "cat", "banana", "dog"]

for i in range(len(li)):
    for j in range(0, len(li) - i - 1):
        if len(li[j]) > len(li[j + 1]):
            temp = li[j]
            li[j] = li[j + 1]
            li[j + 1] = temp

print("Sorted list:", li)