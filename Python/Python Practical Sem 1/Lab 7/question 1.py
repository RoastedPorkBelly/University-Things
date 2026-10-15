number = int(input("Enter a number between 1 and 12: "))

if 1 <= number <= 12:
    print(f"Multiplication table for {number}:")

    for i in range (1,13):
        result = number * i
        print(f"{number} x {i} = {result}")

else:
    print("Please enter a valid number between 1 and 12.")