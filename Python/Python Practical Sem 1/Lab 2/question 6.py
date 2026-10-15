day = (input("Input a number that corresponds to the day of the week, e.g. Monday = 1: "))
#when float isn't input, then it defaults to string

match day:
    case '1':
        print('Monday: Peppermint Mocha')

    case '2':
        print('Tuesday: Candy Bar Latte')

    case '3':
        print('Wednesday: Caramel Coffee')

    case '4':
        print('Thursday: Chocolate Almond Cafe Au Lait')
    
    case '5':
        print('Friday: Pumpkin-Chai Latte')

    case '6':
        print('Saturday: Vanilla Chai Tea')
    
    case '7':
        print('Sunday: Gingerbread Latte')
    
    case _:
        print('Invalid Entry')