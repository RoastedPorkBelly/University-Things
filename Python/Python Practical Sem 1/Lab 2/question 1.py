rentNew = float(input("Number of New: "))
rentOld = float(input("Number of Old: "))
rentDays = float(input("Number of Days: "))
newRate = 3.00
old_rate = 2.00

total = ((rentOld*old_rate)+(rentNew*newRate))*rentDays
print("Total cost: ", total)