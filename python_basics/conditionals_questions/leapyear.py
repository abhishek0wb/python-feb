year = int(input("enter year to check \n"))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("this is a leap year")

else : 
    print("this is not a leap year")     