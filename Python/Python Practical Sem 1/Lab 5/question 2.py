number = int(input("What number multiplication table would you like to print? "))
limit = int(input("How high would you like it to go? "))

print("Here is your multiplication table: ")

i = 1

while i <= limit:
    print(number, "times", str(i).ljust(2), "=", str(number*i).rjust(3))
    i += 1