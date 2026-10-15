#Write a function named collatz() that has one parameter named number. 
# If number is even, then collatz() should print number // 2 and return this value. 
# If number is odd, then collatz() should print and return 3 * number + 1.

def collatz(number):
    if number % 2 == 0:
        value = number // 2
    else: 
        value = 3 * number + 1

    print(value, end =" ")
    return value 

try: 
    num = int(input("Enter an integer: ")) 
    while num !=1:
        num = collatz(num)
except ValueError:
    print("Invalid input")



    