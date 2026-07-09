#WAP to calculate selling price of book based on cost price and discount.
# Discount = (Cost Price × Discount %) / 100
# Selling Price = Cost Price − Discount
cp = float(input("Enter Cost Price:"))
discount = float(input("Enter Discount (%):"))

discount_amount = (cp * discount) / 100
sp = cp - discount_amount

print("Selling Price =", sp)