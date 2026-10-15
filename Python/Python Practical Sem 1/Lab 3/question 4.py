total = 0
#placeholder total
n = input("enter a number of type 'DONE': ").upper()

#the .upper() is to foolproof the code in case "done" is written instead of "DONE"

while n != 'DONE':
#while n is NOT EQUAL to 'DONE'

    num = int(n)
#exclusion: string conversion to integer

    total = total + num
    #real total
    n = input("Enter a number of tpe: 'DONE': ").upper()

print('The sum of the numbers are: ', total)

'''
for some reason all values that say "total" must be the same.
i tried changing placeholder total to "zero" and the code broke
'''