a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

power=1
i=1
#initialization values

while i <=b:
    power=power*a
    i=i+1
else:
    print (str(a), 'to the power of', str(b), 'is', str(power))

'''
explanation:

example values:
a= 2, b=3

(1) while loop runs
p = p*a     i = i+1
p = 1*2=2   i = 1+1 = 2

i is still less than/equal to 3, while loop runs again
'''
#(2)
#p= 2x2 = 4, i= 2+1 = 3
#while loop runs again


# p = 4x2 = 8, i = 3+1 = 4
#while loop WILL NOT run again, 8 is output