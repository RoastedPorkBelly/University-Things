import random, sys

# for i in range(5):
#     print(random.randint(1,100))

# while True:
#     print("Type 'exit' to exit.")
#     response = input(" ")
#     if response == "exit":
#         sys.exit()
#     print ("Program exited")

print ("I am thinking of a number between 1 and 20.")
number = random.randint(1,20)

for attempts in range(1,7):
    guess = int(input("Take a guess: "))

    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else: 
        break

if guess == number:
    print("That is the correct answer! You got it in " + str(attempts) + " attempts.")
else:
    print("Too many tries! The number is: " + str(number))
