answer = input("Do you want to play this game ? [Yes/No] : ")

myStr = answer.lower();

if myStr == 'yes' | myStr == 'y':
    print("welcome to the game!")
    answer = input('do you want to go jungle [j/m]')
    if answer == "j":
        print('Your are in jungle')
else:
    print("Game closed")