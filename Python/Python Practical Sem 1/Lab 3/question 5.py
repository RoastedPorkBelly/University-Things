import random
secretNumber = random.randint(1,50)
print(secretNumber)
#unrelated to question 


c= 1
guessTheNumber = int(input("Guess the secret number:"))

while guessTheNumber != secretNumber:
    if guessTheNumber <= secretNumber:
        print('Too Low')
    else:
        print ('Too High')
    c= c+1
    guessTheNumber = int(input("Guess again: "))

print ("You took " + str(c) + " attempts")
