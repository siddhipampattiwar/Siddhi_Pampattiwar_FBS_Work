# Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.
n = int(input("Enter Number of Students = "))

avg = 0

for i in range(1, n + 1):
    print("\nStudent", i)

    total = 0

    for j in range(1, 6):
        marks = int(input("Enter Marks of Subject {} = ".format(j)))
        total = total + marks

    per = total / 5
    print("Percentage =", per)

    avg = avg + per

print("\nAverage Percentage of Students =", avg / n)