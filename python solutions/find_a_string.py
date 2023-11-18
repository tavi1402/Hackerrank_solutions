# Define a function named count_substring that takes two arguments: string and sub_string.
def count_substring(string, sub_string):
    # Initialize a variable 'count' to keep track of the number of occurrences of sub_string in string.
    count = 0
    
    # Loop through the indices of the 'string' where the sub_string might start.
    # The loop range ensures that we only check substrings of the same length as sub_string.
    for i in range(len(string) - len(sub_string) + 1):
        # Check if the substring of 'string' from index 'i' to 'i + len(sub_string)' is equal to 'sub_string'.
        if string[i:i + len(sub_string)] == sub_string:
            # If they are equal, increment the 'count' variable by 1.
            count += 1

    # After looping through the entire 'string', return the final count of occurrences of 'sub_string'.
    return count

# This part of the code is executed only when the script is run as the main program.
if __name__ == '__main__':
    # Read a string input from the user, remove leading and trailing white spaces, and store it in the 'string' variable.
    string = input().strip()
    
    # Read another string input from the user, remove leading and trailing white spaces, and store it in the 'sub_string' variable.
    sub_string = input().strip()
    
    # Call the 'count_substring' function with the provided 'string' and 'sub_string', and store the result in the 'count' variable.
    count = count_substring(string, sub_string)
    
    # Print the final count, which represents the number of times 'sub_string' appears in 'string'.
    print(count)
