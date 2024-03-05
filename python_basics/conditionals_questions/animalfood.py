animal = input("enter the type of animal \n")
age = int(input("animal age? \n"))

if (age > 5) and (animal=="dog" or "cat"):
    print("senior pet food")

else:
    print("food is not here")