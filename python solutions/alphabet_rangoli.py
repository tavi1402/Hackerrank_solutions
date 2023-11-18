def print_rangoli(size):
    import string
    
    # Create a string containing all lowercase letters of the English alphabet
    design = string.ascii_lowercase
    
    # Initialize an empty list to store the lines of the rangoli pattern
    pattern_lines = []
    
    # Iterate over a range of numbers from 0 to (size-1)
    for i in range(size):
        # Create a string 's' by joining a slice of 'design' from index 'i' to 'size' with hyphens
        s = "-".join(design[i:size])
        
        # Create the central part of the rangoli pattern by reversing 's' and concatenating it with 's' excluding the first character
        central_part = (s[::-1] + s[1:])
        
        # Center the 'central_part' within a string of width '4*size-3' using hyphens as fill characters, and append it to 'pattern_lines'
        pattern_lines.append(central_part.center(4 * size - 3, "-"))
        
    # Print the rangoli pattern by joining the lines in 'pattern_lines', first in reverse order and then in the original order
    print('\n'.join(pattern_lines[:0:-1] + pattern_lines))

if __name__ == '__main__':
    # Read an integer 'n' from the user
    n = int(input())
    
    # Call the 'print_rangoli' function, passing 'n' as the 'size' argument
    print_rangoli(n)
