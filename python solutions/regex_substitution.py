'''this line of code searches for occurrences of '&&' or '||' in the user's input, where each operator is surrounded 
by spaces, and replaces them with 'and' or 'or', respectively. This operation is a way of humanizing or simplifying 
logical expressions, making them more readable or user-friendly. For example, if the user enters "A && B || C," 
the code will replace it with "A and B or C."'''
import re

# Read the number of lines from the standard input
num_lines = int(input())

# Loop through each line
for _ in range(num_lines):
    line = input()
    modified_line = re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', line)
    print(modified_line)
