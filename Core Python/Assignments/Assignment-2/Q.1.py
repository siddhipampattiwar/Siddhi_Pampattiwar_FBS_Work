# Convert the time entered in hh,min and sec into seconds.
hour = int(input("Enter hours: "))
minute = int(input("Enter minutes: "))
second = int(input("Enter seconds: "))

total_seconds = (hour*3600) + (minute * 60) + second
print ("Total Seconds =", total_seconds)