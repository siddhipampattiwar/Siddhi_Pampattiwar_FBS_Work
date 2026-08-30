# Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the
# Python set.
s = {2, 5, 8, 3}

max_product = 0
pair = ()

lst = list(s)

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        product = lst[i] * lst[j]

        if product > max_product:
            max_product = product
            pair = (lst[i], lst[j])

print("Pair:", pair)
print("Maximum product:", max_product)