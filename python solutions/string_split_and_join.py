# Define a function named 'split_and_join' that takes a single argument 'line'.
def split_and_join(line):
    # Split the input string 'line' into a list of words using spaces as separators.
    line = line.split()
    
    # Join the list of words into a single string using hyphens as separators.
    line = "-".join(line)
    
    # Return the resulting string after splitting and joining.
    return line

# If this script is executed as the main program:
if __name__ == '__main__':
    # Read a string 'line' from the user.
    line = input()
    
    # Call the 'split_and_join' function with the input string 'line' and store the result.
    result = split_and_join(line)
    
    # Print the resulting string, which has spaces replaced by hyphens.
    print(result)
