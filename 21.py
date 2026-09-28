age = int(input("Enter the age: "))

if age <=5:
    ticketprice = 0
elif age <=12:
    ticketprice = 100
elif age <=60:
    ticketprice = 200
else:
    ticketprice = 120

print("Ticket Price:", ticketprice)
