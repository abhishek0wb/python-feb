import math

def circle_stats(radius):
    area = math.ceil( math.pi * radius **2)
    cirfer = 2*math.pi * radius
    return area, cirfer

a, c = circle_stats(3)

#  how does know a,c and what they represent

print("Area",a, "Circumfrence", c)