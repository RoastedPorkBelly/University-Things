import os

def display_menu():
    print("[1] Create a new file.")
    print("[2] Display the file.")
    print("[3] Add a new item to the file.")
    
def create_new_file():
    subject = input("Enter a subject (e.g., CSC1024 Programming Principles): ")
    with open("Subject.txt", "w") as file:
        file.write(subject + "\n")
    print("Subject saved to Subject.txt.")

def display_file():
    if os.path.exists("Subject.txt"):
        with open("Subject.txt", "r") as file:
            contents = file.read()
            print("\nContents of Subject.txt:")
            print(contents)
    else:
        print("Error: Subject.txt does not exist.")

def add_new_item():
    if os.path.exists("Subject.txt"):
        new_subject = input("Enter a new subject to add: ")
        with open("Subject.txt", "a") as file:
            file.write(new_subject + "\n")
        print("New subject added.")
        display_file()
    else:
        print("Error: Subject.txt does not exist. Please create the file first.")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter 1, 2, or 3: "))
            if choice == 1:
                create_new_file()
            elif choice == 2:
                display_file()
            elif choice == 3:
                add_new_item()
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Error: Please enter a valid number (1, 2, or 3).")
        
        another = input("\nDo you want to perform another action? (yes/no): ").strip().lower()
        if another != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
