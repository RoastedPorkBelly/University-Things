row = 0

while row < 5:
    column = 0
    while column < 11:
        if column%2 == 0: #check even number
            print('1', end='')
        else:
            print('0', end='')
        column +=1
    print()
    row += 1