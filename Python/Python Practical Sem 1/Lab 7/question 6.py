numbers = []

print("Enter 10 numbers: ")
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

maxNumber = numbers [0]
minNumber = numbers [0]

for num in numbers:
    if num > maxNumber:
        maxNumber = num
    elif num < minNumber:
        minNumber = num

print("Results:")
print(f"The maximum value is {maxNumber}.")
print(f"The minimum value is {minNumber}.")