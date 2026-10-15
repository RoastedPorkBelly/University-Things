# Function to ask the user for a number and save it as 'num'
def get_number():
    num = int(input("Enter a number: "))
    return num

# Function to count from 1 to the given number
def count_to_number(num):
    for i in range(1, num + 1):
        print(i)

# Main program
def main():
    num = get_number()  # Call the first subprogram to get the number
    print(f"Counting from 1 to {num}:")
    count_to_number(num)  # Call the second subprogram to count

# Execute the main program
main()
