# Write a Python program to find all the anagrams and group them
# together from a given list of strings.
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in words:
    key = ''.join(sorted(word))

    if key in groups:
        groups[key].append(word)
    else:
        groups[key] = [word]

print(list(groups.values()))