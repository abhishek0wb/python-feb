import random

top_of_range = input("type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('please type a larger than zero ')
        quit()

else:
    print('please only type number')        


random_number = random.randint(0, top_of_range)
print(random_number)
