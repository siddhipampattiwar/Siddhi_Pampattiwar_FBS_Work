# 1. Find all of the numbers from 1–1000 that are divisible by 8

numbers = [i for i in range(1, 1001) if i % 8 == 0]
print(numbers)

# 2. Find all of the numbers from 1–1000 that have a 6 in them

numbers = [i for i in range(1, 1001) if '6' in str(i)]
print(numbers)

# 3. Count the number of spaces in a string (take input from user)

string = input("Enter a string: ")
count = sum([1 for i in string if i == ' '])
print("Number of spaces =", count)

# 4. Remove all of the vowels in a string (take input from user)

string = input("Enter a string: ")
result = ''.join([i for i in string if i.lower() not in 'aeiou'])
print("String without vowels =", result)

# 5. Find all of the words in a string that are less than 5 letters (take input from user)

string = input("Enter a string: ")
words = [i for i in string.split() if len(i) < 5]
print("Words having less than 5 letters =", words)

# 6. Use a dictionary comprehension to count the length of each word in a sentence (take input from user)

string = input("Enter a sentence: ")
result = {word: len(word) for word in string.split()}
print(result)

# 7. Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit.

numbers = [i for i in range(1, 1001) 
           if any(i % j == 0 for j in range(1, 10))]
print(numbers)

# Assignment on Generator

# 1. We want to generate Fibonacci numbers up to a certain limit.Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one, conserving memory and allowing for easy iteration.

def fibonacci(limit):
    a = 0
    b = 1
    while a <= limit:
        yield a
        a, b = b, a + b
limit = int(input("Enter limit: "))
for num in fibonacci(limit):
    print(num)

# 2. Implement a generator function that yields palindrome numbers.Palindromes are numbers that read the same backward as forward
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.

def palindrome():
    num = 0
    while True:
        if str(num) == str(num)[::-1]:
            yield num
        num += 1
p = palindrome()
for i in range(10):
    print(next(p))

# 3. Write a generator function that mimics the behavior of the built-in range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.

# Assignment of Decorator

# 1. Develop a memoization decorator that caches the results of function calls and returns the cached result when the same inputs occur again.
# This can greatly improve the performance of recursive or computationally intensive functions.

