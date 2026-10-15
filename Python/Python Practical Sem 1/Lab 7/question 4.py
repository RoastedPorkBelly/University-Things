import random

score = 0

for i in range(5):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)

    operator = random.choice(["+","-","*","/"])

    if operator == "+":
        correctAnswer = num1 + num2
    elif operator == "-":
        correctAnswer = num1 - num2
    elif operator == "/":
        correctAnswer = num1/num2
    else:
        correctAnswer = num1*num2
    

    userAnswer = float(input(f"Question {i+1}: What is {num1} {operator} {num2}?"))
    if userAnswer == correctAnswer:
        print("Correct!")
        score +=1
    else:
        print("lmao stupid")
        print(f"The correct answer was {correctAnswer}.")

print (f"Your final score is {score} out of 5!")