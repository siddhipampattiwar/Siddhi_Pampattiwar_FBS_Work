#WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.
# basic → Basic salary of the employee.
# da = (10 * basic) / 100 → Calculates 10% Dearness Allowance.
# ta = (12 * basic) / 100 → Calculates 12% Travel Allowance.
# hra = (15 * basic) / 100 → Calculates 15% House Rent Allowance.
# total_salary = basic + da + ta + hra → Adds all amounts to get the total salary.
# print() → Displays the total salary.

basic = 50000
da = (10 * basic) / 100
ta = (12 * basic) / 100
hra = (15 * basic) / 100
total_salary = basic + da+ ta + hra
print ("Total Salary =", total_salary)