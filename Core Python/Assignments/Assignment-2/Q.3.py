#Convert distant given in feet and inches into meter and centimeter.
# foot = 0.3048 meter
# inch = 2.54 centimeter
feet = float(input(" Enter feet: "))
inches = float(input(" Enter inches: "))

meter = feet * 0.3048
centimeter = inches * 2.54

print("Meter =", meter)
print("Centimeter =", centimeter)