import time, sys

try:
    while True:
        for i in range(1,9): #stops before 9
            print("-" * i**2) #1x2, 2x2, 3x2
            time.sleep(0.1)
        
        for i in range (7, 1, -1): #stops before 0
            print("-" * i**2) 
            time.sleep(0.1)

except KeyboardInterrupt:
     sys.exit