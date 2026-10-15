import random

playGame = True

while playGame:
    secretNumber = random.randint(1,200)
    print(secretNumber) 
    count= 1
    guessTheNumber = int(input("Guess the secret number:"))

while guessTheNumber != secretNumber:

    if guessTheNumber <= secretNumber:
        print('Too Low')
    else:
        print ('Too High')
    count= count + 1
    guessTheNumber = int(input("Guess again: "))

print ("You took " + str(count) + " attempts")

continueGame = input ("Would you like to continue? [Y/N]: ").upper

while continueGame !='N' and continueGame !='Y':
    continueGame = input ("Would you like to continue? [Y/N]: ").upper

if continueGame == 'N':
    playGame = False

