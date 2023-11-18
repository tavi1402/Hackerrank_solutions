# Define a function named 'swap_case' that takes a string 's' as input
def swap_case(s):
    # Initialize an empty string 'num' to store the swapped characters
    num = ""
    
    # Iterate through each character 'let' in the input string 's'
    for let in s:
        # Check if the character is uppercase
        if let.isupper() == True:
            # If it's uppercase, convert it to lowercase and add to 'num'
            num += (let.lower())
        else:
            # If it's not uppercase (i.e., it's lowercase), convert it to uppercase and add to 'num'
            num += (let.upper())
    
    # Return the 'num' string with characters swapped
    return num

# If this script is executed as the main program:
if __name__ == '__main__':
    # Read a string 's' from the user
    s = input()
    
    # Call the 'swap_case' function with the input string 's' and store the result
    result = swap_case(s)
    
    # Print the result (the swapped string) to the screen
    print(result)
