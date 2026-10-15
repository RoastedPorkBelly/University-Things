def read_number(total_num_to_read):
    user_list = []
    for _ in range(total_num_to_read):
        num = float(input("Enter a number: "))
        user_list.append(num)
    return user_list

def find_max_number(a_list_of_num):
    max_num = max(a_list_of_num)
    return max_num

def find_min_number(a_list_of_num):
    min_num = min(a_list_of_num)
    return min_num 

def main():
    total_numbers = int(input("Enter how many numbers you want to read into a list: "))
    numbers_list = read_number(total_numbers)

    max_number = find_max_number(numbers_list)  # Call function to find the maximum number
    min_number = find_min_number(numbers_list)  # Call function to find the minimum number

    # Print results
    print(f"Numbers in the list = {numbers_list}")
    print(f"Maximum Number = {max_number}")
    print(f"Minimum Number = {min_number}")