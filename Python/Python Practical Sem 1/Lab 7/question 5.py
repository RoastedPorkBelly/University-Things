playAgain = "Y"

while playAgain == 'Y':
    print("Temperature Conversion Program")
    print("[1]Convert celcius to Fahrenheit." )
    print("[2]Convert Fahrenheit to Celcius." )

    selection = int(input('Enter your selection (1 or 2): '))
    if selection == 1:
        print("Celcius to Fahrenheit conversion")
        print('Enter temperature in integer values only.')
        temp_min = int(input('Enter minimum temperature: '))
        temp_max = int(input('Enter maximum temperature: '))

        if temp_min <= temp_max:
            temp_celcius = temp_min

            for temp_celcius in range(temp_min, temp_max+1):

                temp_fahrenheit = (temp_celcius*(9/5))*32
                print(f'{(temp_celcius)} Celcius = {(temp_fahrenheit):.1f} Fahrenheit')
            print('Conversion done!')
        else:
            print('ERROR: Invalid Input')

    elif selection ==2:
        print('Fahrenheit (F) to Celcius (C) Conversion')
        print('Enter temperature in integer values only.')
        temp_min = int(input('Enter minimum temperature: '))
        temp_max = int(input('Enter maximum temperature: '))

        if temp_min <= temp_max:

            for temp_fahrenheit in range(temp_min, temp_max+1):

                temp_celcius = (temp_fahrenheit -32) *(5/9)
                print(f"{(temp_fahrenheit)} F = {(temp_celcius):.1f} C")

            print('Conversion done!')
        else:
            print('ERROR: Invalid Input')
    
    else:
        print('Invalid Selection!')

    playAgain = input('Do you want to run the program again? [Y/N]: ').upper()

    while playAgain !='N' and playAgain !='Y':
            playAgain = input('Do you want to run the program again? [Y/N]: ').upper()

print('Program Terminated')

