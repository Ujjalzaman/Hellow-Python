import random

randomNumber = random.randrange(1, 200)
userinput = int(input("Guess the number "))

if userinput > randomNumber:
    print("the number is to high")

elif randomNumber > userinput:
    print("the number is too low")

else:
    print("Number is Matched")