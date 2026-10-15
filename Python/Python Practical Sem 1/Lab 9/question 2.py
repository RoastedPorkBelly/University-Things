def multiplication_table_to_file():
    # Ask the user for a multiplication table
    try:
        number = int(input("Enter the multiplication table you want (e.g., 2 for the 2-times table): "))
        filename = f"TT{number}TXT.txt"

        # Write the multiplication table to a file
        with open(filename, "w") as file:
            file.write(f"Multiplication Table for {number}\n")
            file.write("-" * 30 + "\n")
            for i in range(1, 13):
                file.write(f"{number} x {i} = {number * i}\n")
        print(f"Multiplication table saved to {filename}.")

        # Read and display the file contents
        with open(filename, "r") as file:
            print("\nReading the contents of the file:")
            print(file.read())

    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    multiplication_table_to_file()
