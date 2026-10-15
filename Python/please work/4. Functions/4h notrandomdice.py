import random

def getRandomDiceRoll():
    randomNumber = random.randint(1,6)
    return randomNumber

print(getRandomDiceRoll())
print(getRandomDiceRoll())
print(getRandomDiceRoll())

#global variable is set outside the function and never changes