# Write a program to check if entered year is a leap year or not.
year=int(input('Enter a year:'))
if(year%400==0) or (year%4==0 and year % 100!=0):
    print('Leap Year')
else:
    print('Not a Leap Year')    

# We divide by 4 because the Earth takes about 365.25 days to complete one orbit around the Sun.
# A normal year has 365 days.
# Every year, there is an extra 0.25 day (6 hours).
# After 4 years:
# 0.25 × 4 = 1 day
# So, we add one extra day (February 29) every 4 years. This makes it a Leap Year.    