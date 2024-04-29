word = "Hablue"
chances = 5
guessAdd = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guessAdd:
            print(letter, end = ' ')
        else:
            print("-", end= "")
    
    myGuess = input(f"Your changes is {chances} , gues the letter: ")
    guessAdd.append(myGuess.lower())

    if myGuess.lower() not in word.lower():
        chances -= 1
        if chances == 0:
            break
    
    done = True

    for letter in word:
        if letter.lower() not in guessAdd:
            done = False

if done:
    print(f" yes, you have won the game")
else:
    print("Lose the Game")