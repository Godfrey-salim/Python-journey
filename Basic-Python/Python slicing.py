# Python program that takes in starting index and stopping index, outputs all the numbers in between and after that reverse.
def display_menu():
    print("1. Main Menu")
    print("2. Exit")
    choice = input("Enter your choice (1/2): ")
    return choice
## Get list choice ( enter your own list or use default{1-10})
def get_list_choice():
    while True:
        choice = input("Choose between:\n1. Enter your own list\n2. Use list (1-10) given\nEnter your choice (1/2): ")
        if choice == '1':
            custom_list = input("Enter your list of values separated by commas: ").split(',')
            custom_list = [item.strip() for item in custom_list]
            return custom_list
        elif choice == '2':
            return list(range(1, 11))
        elif choice == 'back':
            return 'back'
        else:
            print("Invalid choice. Please enter 1 or 2.")
## Get the slicing indices (start of the slice and stopping of the slice)
def get_slice_indices():
    while True:
        try:
            start_index = input("Enter the starting index of the slice: ")
            stop_index = input("Enter the stopping index of the slice: ")
            if start_index == "":
                start_index = None
            else:
                start_index = int(start_index)
            if stop_index == "":
                stop_index = None
            else:
                stop_index = int(stop_index)
            return start_index, stop_index
        except ValueError:
            print("Invalid input. Please enter valid integers or leave blank for default.")
## slice results and reverse option
def reverse_option(slice_result):
    while True:
        choice = input("Reverse:\n1. Yes\n2. No\nEnter your choice (1/2): ")
        if choice == '1':
            print("Reversed Slice:")
            print(slice_result[::-1])
            break
        elif choice == '2':
            print("No reversal chosen. Program ends.")
            break
        elif choice == 'back':
            return 'back'
        else:
            print("Invalid choice. Please enter 1 or 2.")
## The main menu after back option is activated or at the end of the program.
def main_menu():
    while True:
        list_choice = get_list_choice()
        if list_choice == 'back':
            continue
        print(f"List chosen: {list_choice}")
        
        start_index, stop_index = get_slice_indices()
        slice_result = list_choice[start_index:stop_index]
        print(f"Slice result: {slice_result}")
        
        if reverse_option(slice_result) == 'back':
            continue
        
        choice = display_menu()
        if choice == '1':
            continue
        elif choice == '2':
            print("Thank you 😊👍")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main_menu()
