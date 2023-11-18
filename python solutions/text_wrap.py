import textwrap

def wrap(string, max_width):
    # Initialize a loop that iterates in steps of 'max_width' from 0 to the length of the 'string'.
    for i in range(0, len(string) + 1, max_width):
        # Slice the 'string' to get a segment of 'max_width' characters.
        result = string[i:i+max_width]
        
        # Check if the length of 'result' is equal to 'max_width'.
        if len(result) == max_width:
            # If it is, print 'result' as it's a complete line.
            print(result)
        else:
            # If it's not, return 'result' (it's the last partial line).
            return result

if __name__ == '__main__':
    # Get user input for 'string' and 'max_width'.
    string, max_width = input(), int(input())
    
    # Call the 'wrap' function with 'string' and 'max_width'.
    result = wrap(string, max_width)
    
    # Print the result.
    print(result)
