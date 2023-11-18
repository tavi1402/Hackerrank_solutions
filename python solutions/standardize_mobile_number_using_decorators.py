'''The main purpose of this code is to sort and format a list of phone numbers. 
The wrapper decorator modifies the behavior of the sort_phone function by adding a country code and 
formatting the numbers in a specific way before sorting and printing them.'''

def wrapper(f):
    # Define a decorator function 'wrapper' that takes another function 'f' as an argument.
    def fun(l):
        # Define an inner function 'fun' that takes a list 'l' as an argument.
        # This function processes the input list 'l' before passing it to the original function 'f'.
        f(["+91 " + c[-10:-5] + " " + c[-5:] for c in l])
        # Modify each element 'c' in the list 'l' by adding '+91 ' to the beginning
        # and formatting it as '+91 ABCDE FGHIJ', where 'A', 'B', 'C', 'D', 'E' represent
        # the first five digits, and 'F', 'G', 'H', 'I', 'J' represent the last five digits.

    return fun  # Return the inner function 'fun' as the result of the 'wrapper' function.

@wrapper
# Apply the 'wrapper' decorator to the 'sort_phone' function.
def sort_phone(l):
    # Define the 'sort_phone' function that takes a list 'l' as an argument.
    print(*sorted(l), sep='\n')
    # Sort the elements in the list 'l' and print them with each number separated by a newline character.

if __name__ == '__main__':
    # Check if the script is run as the main program (not imported as a module).
    l = [input() for _ in range(int(input()))]
    # Read an integer from the user indicating the number of phone numbers to input,
    # and read the phone numbers as input using a list comprehension.

    sort_phone(l)
    # Call the 'sort_phone' function with the list of phone numbers as an argument.
    # This function has been decorated with 'wrapper', so the phone numbers will be formatted and sorted.
