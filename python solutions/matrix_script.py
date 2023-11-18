'''this code takes user input to create a 2D grid of characters, converts it into a 1D string, and then inserts 
spaces between special characters that are adjacent to alphanumeric characters using regular expressions.'''
# Import the 're' module for regular expressions
import re

# Read two integers 'n' and 'm' from user input
n, m = map(int, input().split())

# Initialize a list 'character_ar' with empty strings, total length is 'n * m'
character_ar = [''] * (n * m)

# Loop over 'n' rows
for i in range(n):
    # Read a line of characters from user input
    line = input()
    
    # Loop over 'm' characters in the line
    for j in range(m):
        # Assign each character from the input line to the 'character_ar' list
        character_ar[i + (j * n)] = line[j]

# Join the characters from the list into a single string
decoded_str = ''.join(character_ar)

# Use regular expressions to replace sequences of special characters with spaces
final_decoded_string = re.sub(r'(?<=[A-Za-z0-9])([ !@#$%&]+)(?=[A-Za-z0-9])', ' ', decoded_str)

# Print the final decoded string
print(final_decoded_string)
