playing= input("Do you want to play? (y,n) ")

if playing !="y":
    quit()

print("okay welcome to computer quiz!!")
Score=0

question = input("Q2: which Year was Facebook birth? \nAnswer ")
if question == "2004":
    print("Correct")
    Score += 1
else:
    print("incorrect")


question = input("Q3: which Galaxy in which earth is? \nAnswer ").lower()
if question == "milkway":
    print("Correct")
    Score += 1
else:
    print("incorrect")


question = input("Q3: which planet do we live? \nAnswer ").lower()
if question == "earth":
    print("Correct")
    Score += 1
else:
    print("incorrect")




print("Your got " + str(Score)+ " Questions correct!")