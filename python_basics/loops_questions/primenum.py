num = 7

prime = True

if num >1:
   for i in range(2, num):
       if num % i == 0:
           prime = False
           break
       
print(prime)       