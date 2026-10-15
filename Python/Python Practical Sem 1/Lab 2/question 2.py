elapsedTime = int(input("Elapsed Time in seconds: "))

#the // sign rounds down the remainder 
#the %(modulus) sign calculates the Remainder


hours = elapsedTime//3600
#round down remainder and divide by 3600 (cuz 1 hour is 3600 seconds)
remainderMins = elapsedTime - (3600*hours)
#remainder is time - the hours
minutes = remainderMins//60
#round down remainder and divide by 60

seconds = remainderMins%60
#calculate remainder and divide by 60

print(str(hours).rjust(2, '0') + ":" + str(minutes).rjust (2, '0') + ":" + str(seconds).rjust(2, '0'))

#rjust = adjusts the value to the right, so if
#u write "2", then it'll show up as "02"

##rjust(2, '0')
#this adjusts the value to the right, and fills in the empty space with a '0'