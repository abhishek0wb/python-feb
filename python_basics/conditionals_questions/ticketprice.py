age = int(input("enter your age? \n"))

day = "monday"

price = 12 if age>18 else 8

if day == "wednesday":
    price = price - 2


print("Ticket price for you $",price)