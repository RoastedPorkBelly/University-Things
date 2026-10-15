import time, sys
indent = 0 #spaces to indent
indentIncreasing = True #increase spaces or not

try:
    while True:
        print(" " * indent, end="")
        print('********')
        time.sleep(0.1) #adds delay 

        if indentIncreasing: #increase spaces
            indent +=1
            if indent == 20:
                indentIncreasing = False
        else: #decrease spaces
            indent -=1
            if indent == 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit