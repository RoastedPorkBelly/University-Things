playGame = input("Would you like to count UP or DOWN?").upper()

if playGame == "UP" :
    ask = int(input("Input number to count to: "))
    for i in range (1,ask+1,1):
        print(i)

elif playGame == "DOWN" :
    askDown = int(input("Input number to count down from 20: "))
    if askDown < 20:
        for i in range (20, askDown-1, -1):
            print(i)
    else:
        print("Invalid input.") 

else:
    print("Invalid input.")