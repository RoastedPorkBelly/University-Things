import math
choice = input("Choose 'R' or 'r' for rectangle and 'C' or 'c' for circle: ").lower()

#choice = input('stuff').lower()
##this will make it so that when an uppercase letter is input, then it will be converted into a lowercase letter.

if choice == 'r':
    
#the '=' sign means "it is true". this won't work because r hasnt been defined yet
#the == sign checks if (choice) is equal to (r)
    l = float(input("Length: "))
    w = float(input("Width: "))
    print (f'The area is {(l*w):.2f}')

if choice == 'c':
    rad = float(input("radius: "))
    print(f'The area is {(2*math.pi*rad**2):.2f}')

'''
Explanation of .2f:
.: This indicates that you are about to specify the precision for the floating-point number.
2: This number specifies the number of decimal places to include in the output. In this case, it means the output will be rounded to two decimal places.
f: This stands for floating-point number. It indicates that the number being formatted is a float.
'''
