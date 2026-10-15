import random

def addition():
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)

    print(f"Add: {num1} + {num2}")

    correctAnswer = num1 + num2
    userAnswer = int(input("Your answer here: "))
    return(userAnswer, correctAnswer)

def subtraction():
    num1 = random.randint(25,50)
    num2 = random.randint(1,25)

    print(f"Subtract {num1} - {num2} ")

    correctAnswer = num1 - num2
    userAnswer = int(input("Your answer here: "))
    return(userAnswer, correctAnswer)

def checkAnswer(userAnswer, correctAnswer):
    if userAnswer == correctAnswer:
        print("Correct!")
    else: 
        print(f"Incorrect, the answer is {correctAnswer}.")

def main():
    print("[1] Addition")
    print ("[2] Subtraction")
    choice = int(input("Enter 1 or 2: "))

    if choice == 1:
        userAnswer, correctAnswer = addition()
        checkAnswer(userAnswer, correctAnswer)


    elif choice == 2:
        userAnswer, correctAnswer = subtraction()
        checkAnswer(userAnswer, correctAnswer)

    else: 
        print("Enter a valid option (1 or 2).")

main()
    
