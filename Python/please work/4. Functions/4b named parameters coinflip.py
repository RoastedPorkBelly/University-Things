import random


def coinflip():

    for i in range(0, 10):
        if random.randint(1,2) == 1:
            print("H", end=' ')
        else:
            print("T", end=' ')
    
coinflip()

