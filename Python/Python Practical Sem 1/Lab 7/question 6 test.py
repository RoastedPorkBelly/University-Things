# Initialize an empty list to store the numbers
numbers = []

# Read 10 numbers from the user
print("Enter 10 numbers:")
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Initialize max and min to the first element of the list
max_num = numbers[0]
min_num = numbers[0]

# Traverse the list to find the maximum and minimum
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

# Output the results
print("\nResults:")
print(f"The maximum number is: {max_num}")
print(f"The minimum number is: {min_num}")
