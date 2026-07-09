# WAP to convert days into years, weeks and days.

day = int(input("Enter Days :"))

year = day // 365

remaining = day % 365

week = remaining // 7

days = remaining % 7

print("You Enter = ", day)

print("Year = ", year)

# print(remaining)

print("Week =", week)

print("Days = ", days)
 
 


    