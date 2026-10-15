import os

def display_menu():
    print("Student Grade Manager")
    print("[1] Add new student grades")
    print("[2] View all grades")
    print("[3] Calculate class average")
    print("[4] Exit")

def add_new_grades():
    try:
        name = input("Enter student name: ").strip()
        grade = float(input("Enter student grade (0-100): "))
        if 0 <= grade <= 100:
            with open("grades.txt", "a") as file:
                file.write(f"{name},{grade}\n")
            print(f"Grade for {name} added.")
        else:
            print("Error: Grade must be between 0 and 100.")
    except ValueError:
        print("Error: Invalid input. Grade must be a number.")

def view_all_grades():
    if os.path.exists("grades.txt"):
        print("\nAll Grades:")
        with open("grades.txt", "r") as file:
            for line in file:
                name, grade = line.strip().split(",")
                print(f"{name}: {grade}")
    else:
        print("Error: No grades found. The file does not exist.")

def calculate_class_average():
    if os.path.exists("grades.txt"):
        try:
            total, count = 0, 0
            with open("grades.txt", "r") as file:
                for line in file:
                    _, grade = line.strip().split(",")
                    total += float(grade)
                    count += 1
            if count > 0:
                average = total / count
                print(f"Class Average: {average:.2f}")
            else:
                print("Error: No grades available to calculate average.")
        except ValueError:
            print("Error: Invalid data in the file.")
    else:
        print("Error: No grades found. The file does not exist.")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                add_new_grades()
            elif choice == 2:
                view_all_grades()
            elif choice == 3:
                calculate_class_average()
            elif choice == 4:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
        except ValueError:
            print("Error: Please enter a valid number (1-4).")

if __name__ == "__main__":
    main()