# Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.
words = ["cat","dog","cat","mouse","dog","chiku"]
unique_words = set(words)
for word in unique_words:
    count = 0

    for w in words:
        if word == w:
            count += 1

    print(word, ":", count)        