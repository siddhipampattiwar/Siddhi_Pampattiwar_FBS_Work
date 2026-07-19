# Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
totalPrice = 0

# First Person
ag1 = int(input("Enter the age of First Person = "))
tkprice1 = float(input("Enter the Ticket price for the First Person = "))

if ag1 < 12:
    totalPrice = totalPrice + (tkprice1 * 0.70)      # 30% discount
elif ag1 > 59:
    totalPrice = totalPrice + (tkprice1 * 0.50)      # 50% discount
else:
    totalPrice = totalPrice + tkprice1

# Second Person
ag2 = int(input("Enter the age of Second Person = "))
tkprice2 = float(input("Enter the Ticket price for the Second Person = "))

if ag2 < 12:
    totalPrice = totalPrice + (tkprice2 * 0.70)
elif ag2 > 59:
    totalPrice = totalPrice + (tkprice2 * 0.50)
else:
    totalPrice = totalPrice + tkprice2

# Third Person
ag3 = int(input("Enter the age of Third Person = "))
tkprice3 = float(input("Enter the Ticket price for the Third Person = "))

if ag3 < 12:
    totalPrice = totalPrice + (tkprice3 * 0.70)
elif ag3 > 59:
    totalPrice = totalPrice + (tkprice3 * 0.50)
else:
    totalPrice = totalPrice + tkprice3

# Fourth Person
ag4 = int(input("Enter the age of Fourth Person = "))
tkprice4 = float(input("Enter the Ticket price for the Fourth Person = "))

if ag4 < 12:
    totalPrice = totalPrice + (tkprice4 * 0.70)
elif ag4 > 59:
    totalPrice = totalPrice + (tkprice4 * 0.50)
else:
    totalPrice = totalPrice + tkprice4

# Fifth Person
ag5 = int(input("Enter the age of Fifth Person = "))
tkprice5 = float(input("Enter the Ticket price for the Fifth Person = "))

if ag5 < 12:
    totalPrice = totalPrice + (tkprice5 * 0.70)
elif ag5 > 59:
    totalPrice = totalPrice + (tkprice5 * 0.50)
else:
    totalPrice = totalPrice + tkprice5

print("Total Ticket Price =", totalPrice)