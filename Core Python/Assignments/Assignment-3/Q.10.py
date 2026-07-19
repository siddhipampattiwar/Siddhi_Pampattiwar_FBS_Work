# Write a program to check if person is eligible to marry or not (male age >=21 and
# female age>=18)
age1  = int(input("Enter Male Age = "))
age2 = int(input("Enter Female Age = "))
if age1>=21 and age2>=18:
    print("Eligible for Marriage")  
else:
    print("Not Eligible for Marriage")

# Check Male and Female eligibility separately

male = int(input("Enter Male Age = "))
female = int(input("Enter Female Age = "))

if male >= 21:
    print("Male is Eligible for Marriage")
else:
    print("Male is Not Eligible for Marriage")

if female >= 18:
    print("Female is Eligible for Marriage")
else:
    print("Female is Not Eligible for Marriage")
