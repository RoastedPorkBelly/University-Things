import random

def randomNumber():
    lower = int(input("Enter a number: "))
    higher = int(input("Enter a number higher than the first number: "))
    comp_num = random.randint(lower,higher)
    print (comp_num)
    return comp_num
    
def guessNumber():
    print ("I am thinking of a number... ")
    guess = int(input("Guess the number i am thinking of: "))
    return guess
    

def correctOrNah(comp_num):
    while True:
        guess = guessNumber()
        if guess == comp_num:
            print ("Correct, you win!")
            break
        elif guess > comp_num:
            print ("try lower")
        else:
            print("try higher")

def main():
    comp_num = randomNumber()
    correctOrNah(comp_num)

main()


