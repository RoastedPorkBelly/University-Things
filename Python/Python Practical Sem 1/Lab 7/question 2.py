number = int(input("Enter a number below 50: "))

if number < 50:
    print(f"Counting down from 50 to {number}:")

    for i in range (50,number-1,-1):
        print(i)

else:
    print("Please enter a valid number below 50.")