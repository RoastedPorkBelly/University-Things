# A gigabyte (GB) is 1,073,741,824 bytes.
# A terabyte (TB) is 1,099,511,627,776 bytes.
# However, hard drive and flash memory manufacturers blatantly lie about what these terms mean. 
# For example, 
# by calling a TB 1,000,000,000,000 bytes instead of 1,099,511,627,776 bytes, they can advertise a 9.09TB hard drive as 10TB.

print ("Enter TB or GB for the advertised product: ")
unit = input(">")

# Calculate the "missing bytes" from the false advertising:
if unit == 'TB':
    discrepancy = 1000000000000 / 1099511627776 
    #1 fake TB divided by 1 real TB  =  amount of bytes in a real TB = 0.9TB

elif unit == 'GB': 
    discrepancy = 1000000000 / 1073741824

else: 
    print("Enter a valid input.")
    exit()

fakeAmount = float(input("Enter the advertised capacity: "))
realCapacity = str(fakeAmount * discrepancy)

print("The real capacity is: " + realCapacity + " bytes" )