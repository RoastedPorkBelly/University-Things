import random, sys

print ("ROCK, PAPER, SCISSORS")

wins = 0
losses = 0
ties = 0

while True:
    print(f"{wins} WINS {losses} LOSSES {ties} TIES")

    while True:
        playerChoice = input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit: ")
        if playerChoice == "q":
            sys.exit()
        if playerChoice == "r" or playerChoice == "p" or playerChoice == "s":
            break

    if playerChoice == "r":
        print("Rock vs...")

    elif playerChoice == "p":
        print("Paper vs...")

    elif playerChoice == "s":
        print("Scissors vs...")
    
    computerChoice = random.randint(1,3)
    if computerChoice == 1:
        computerChoice = "r"
        print("Rock!")
    elif computerChoice ==2:
        computerChoice = "p"
        print("Paper!")
    elif computerChoice == 3:
        computerChoice = "s"
        print("Scissors!")

    if playerChoice == computerChoice:
        print("It's a tie!")
        ties +=1
    elif playerChoice == "r" and computerChoice == "p":
        print("You lose!")
        losses +=1
    elif playerChoice == "p" and computerChoice == "s":
        print("You lose!")
        losses +=1
    elif playerChoice == "s" and computerChoice == "r":
        print("You lose!")
        losses +=1
    elif playerChoice == "r" and computerChoice == "s":
        print("You win!")
        wins +=1
    elif playerChoice == "p" and computerChoice == "r":
        print("You win!")
        wins +=1
    elif playerChoice == "s" and computerChoice == "p":
        print("You win!")
        wins +=1

   