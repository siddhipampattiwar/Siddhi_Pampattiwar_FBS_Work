# Write a program to enter P, T, R and calculate simple Interest.
# p*r*t / 100

principle = int(input("Principle Amount :"))
time = int(input("Time :"))
rate = int(input("Enter Rate :"))

simple_interest = (principle * time * rate / 100)

print(f"Simple Interest is : {simple_interest}, Principle Amount is : {principle}, Time is : {time}, Rate is : {rate}" )

