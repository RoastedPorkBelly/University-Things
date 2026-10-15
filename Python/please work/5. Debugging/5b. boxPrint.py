def boxPrint(symbol, width, height):
    if len(symbol) !=1:
        raise Exception ("Symbol must be a single character string.")
    if width <= 2:
        raise Exception ("Width must be greater than 2")
    if height <= 2:
        raise Exception ("Height must be greater than 2")
    
    print (symbol * width) #top of box
    for i in range (height - 2): #run (height-2) times
        print(symbol + (" " * (width - 2)) + symbol) #space * (width-2) times
    print (symbol * width) #bottom of box

try:
    boxPrint('*', 4, 4)
    boxPrint('O', 20, 5)
    boxPrint('x', 1, 3)
    boxPrint('ZZ', 3, 3)
except Exception as err:
    print("An exception happened: "+ str(err))

#last one is not called because: 
#when except clause is executed it does not return to the try clause
try:
    boxPrint('ZZ', 3, 3)
except Exception as err:
    print("An exception happened: "+ str(err))

