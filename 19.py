Amount = 15000

if Amount >= 10000:
    discount = Amount * 20/100
elif Amount >= 5000:
    discount = Amount * 15/100
elif Amount >= 2000:
    discount = Amount * 10/100
else:
    discount = 0
final_amount = Amount - discount
print ("Final Amount:", final_amount)
print ("Discount:", discount)
