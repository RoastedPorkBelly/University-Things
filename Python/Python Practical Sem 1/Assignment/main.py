import os
from datetime import datetime

LOW_STOCK_THRESHOLD = 100

def display_menu():
    print("[1] Add a new supplier.")
    print("[2] Display current inventory levels for all products.")
    print("[3] Add a new product to the inventory.")
    print("[4] Update an existing product.")
    print("[5] Place an order for an existing product.")
    print("[6] Generate Reports.")
    print("[7] Exit Program.")
    
def add_new_supplier():
    if os.path.exists("Assignment/Data/suppliers.txt"):
        new_supplier = input("Enter a new supplier to add: ")
        supplier_id = input("Enter Supplier ID: ")
        contact = input("Enter contact details: ")

        with open("Assignment/Data/suppliers.txt", "a") as file:
            file.write(f"Supplier Name: {new_supplier}, Supplier ID: {supplier_id}, Contact Details: {contact}\n")

        print("New supplier added.")
        display_suppliers()
    else:
        print("Error: suppliers.txt does not exist. Please create the file first.")

def display_suppliers():
    if os.path.exists("Assignment/Data/suppliers.txt"):
        with open("Assignment/Data/suppliers.txt", "r") as file:
            contents = file.readlines()
            print("\nContents of suppliers.txt:")
            print("".join(contents))
    else:
        print("Error: suppliers.txt does not exist.")

def add_new_product():
    if os.path.exists("Assignment/Data/products.txt"):
        new_product = input("Enter a new product to add: ").strip().upper()
        new_id = input("Assign a Product ID: ")
        new_quantity = input("Enter a quantity for the product: ").strip()
        new_price = input("Set a price for the product: ").strip()

        with open("Assignment/Data/products.txt", "a") as file:
            file.write(f"{new_product}, {new_quantity}, ${float(new_price):.2f}, Product ID: {new_id}\n")

        print("New product added.")
        display_products()
    else:
        print("Error: products.txt does not exist. Please create the file first.")

def display_products():
    if os.path.exists("Assignment/Data/products.txt"):
        with open("Assignment/Data/products.txt", "r") as file:
            contents = file.readlines()
            print("\nDisplay current inventory levels for all products:")
            print("".join(contents))
    else:
        print("Error: products.txt does not exist.")

def update_product_details():

    #display products code
    if os.path.exists("Assignment/Data/products.txt"):
        with open("Assignment/Data/products.txt", "r") as file:
            contents = file.readlines()
            print("\nDisplay current inventory levels for all products:")
            print("".join(contents))
    else:
        print("Error: products.txt does not exist.")

    # Ask the user for the product to update
    product_name = input("\nEnter the name of the product to update: ").strip().upper()

    # Search for the product
    found = False
    for i, product in enumerate(contents):
        details = product.strip().split(", ")
        if details[0].lower() == product_name.lower():  # Compare product names (case insensitive)
            found = True
            print(f"\nProduct found: {product.strip()}")

            # Ask for new details            
            details[0] = input("Enter the new product name: ").strip().upper()
            details[1] = int(input("Enter the new quantity: ").strip())  # Update the quantity at index 1
            details[2] = float(input("Enter the new price: ").strip())  # Update the price at index 2
            details[3] = int(input("Enter the new Product ID: ").strip()) # Update the product ID at index 3

            # Update the product details
            contents[i] = f"{details[0]}, {details[1]}, ${details[2]:.2f}, Product ID: {details[3]}\n"
            print("\nProduct updated successfully!")
            break

    if not found:
        print("Error: Product not found.")

    # Write the updated list back to the file
    with open("Assignment/Data/products.txt", "w") as file:
        file.writelines(contents)

    # Confirm update
    print("\nUpdated Product List:")
    display_products()

def place_order():
    #display products code
    if os.path.exists("Assignment/Data/products.txt"):
        with open("Assignment/Data/products.txt", "r") as file:
            contents = file.readlines()
            print("\nDisplay current inventory levels for all products:")
            print("".join(contents))
    else:
        print("Error: products.txt does not exist.")

    # Ask the user for the product name and quantity to order
    product_name = input("\nEnter the name of the product you want to order: ").strip()

    # Search for the product
    found = False
    for i, product in enumerate(contents):
        details = product.strip().split(", ")
        if details[0].lower() == product_name.lower():  # Compare product names (case insensitive)
            found = True
            print(f"\nProduct found: {product.strip()}")
            
            # Variables placed here for better error validation
            available_quantity = int(details[1])
            price_per_unit = float(details[2].strip("$"))
            order_quantity = int(input("Enter the quantity you want to order: ").strip())
            order_id = int(input("Enter your order ID (must be a number): "))
            order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  

            # Add the ordered quantity from the stock
            new_quantity = available_quantity + order_quantity
            contents[i] = f"{details[0]}, {new_quantity}, ${float(price_per_unit):.2f}, {details[3]}\n"


            # Write the updated product list back to the file
            with open("Assignment/Data/products.txt", "w") as file:
                    file.writelines(contents)
            print("The order has been placed, and the stock has been updated.")

            #Append the order back to the file
            ordered = f"{details[3]}, Order ID: {order_id}, Quantity Ordered: {order_quantity}, Time Ordered: {order_time} \n"
            
            with open("Assignment/Data/orders.txt", "a") as file:
                file.writelines(ordered)


    if not found:
        print("\n==Error: Product not found.==")

    # Display updated product list
    print("\nUpdated Product List:")
    display_products()
    
def generate_low_stock_report():
    if os.path.exists("Assignment/Data/products.txt"):
        with open("Assignment/Data/products.txt", "r") as file:
            products = file.readlines()

        print("\nLow Stock Items:")
        for product in products:
            details = product.strip().split(", ")
            product_name = details[0]
            quantity = int(details[1])
            if quantity < LOW_STOCK_THRESHOLD:  
                print(f"{product_name}: {quantity} in stock")
    else:
        print("Error: products.txt does not exist.")

def generate_sales_report():
    if os.path.exists("Assignment/Data/sales.txt"):
        with open("Assignment/Data/sales.txt", "r") as file:
            contents = file.readlines()
            print("\nProduct Sales Report:")
            print("".join(contents))
    else:
        print("Error: sales.txt does not exist.")

def generate_supplier_orders_report():
    if os.path.exists("Assignment/Data/orders.txt"):
        with open("Assignment/Data/orders.txt", "r") as file:
            contents = file.readlines()
            print("\nProduct Orders Report:")
            print("".join(contents))
    else:
        print("Error: orders.txt does not exist.")

def ask_to_exit():
    exit_choice = input("\nDo you want to perform another action? (yes/no): ").strip().lower()
    if exit_choice != "yes":
        print("Goodbye!")
        return True  # Indicate that the program should exit
    return False  # Indicate that the program should continue
        
def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter an option (1-7): "))
            if choice == 1:
                add_new_supplier()
            elif choice == 2:
                display_products()
            elif choice == 3:
                add_new_product()
            elif choice == 4:
                update_product_details()
            elif choice == 5:
                place_order()
            elif choice == 6:
                print("\nGenerate Reports")
                print("[1] Low Stock Report")
                print("[2] Sales Report")
                print("[3] Supplier Orders Report")
                try:
                    report_choice = int(input("Select a report to generate (1-3): "))
                    if report_choice == 1:
                        generate_low_stock_report()
                    elif report_choice == 2:
                        generate_sales_report()
                    elif report_choice == 3:
                        generate_supplier_orders_report()
                    else:
                        print("Invalid choice. Please enter a number between 1 and 3.")
                except ValueError:
                    print("Error: Please enter a valid number for the report.")
            elif choice == 7:
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Enter a number between 1 and 7.")
        except ValueError:
            print("Error: Please enter a valid number.")
        
        if choice != 7 and ask_to_exit():
            break

if __name__ == "__main__":
    main()