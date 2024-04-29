import random

diceRoling = True

while diceRoling:
    print(random.randint(1, 6))
    playagain = input("Do you want to Roll again [y/n]")
    
    if playagain == 'y':
        continue
    else:
        print("Game Over")
        break
