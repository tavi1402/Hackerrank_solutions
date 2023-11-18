'''The provided Python script extracts and accumulate HTML or XML-like tags from a given input. 
It uses a regular expression to find tags and then outputs the unique tags in a sorted, semicolon-separated 
format. Let's break down the code:'''

import re

# Define the regular expression pattern to find HTML or XML-like tags
pat = r'<([a-z0-9]+)'

# Read the number of lines to process
n = int(input())

# Initialize a set to store unique tags
res = set()

# Loop through each line of input
for _ in range(n):
    # Read a line of input
    inp = input()

    # Find all tags in the input using the regular expression pattern
    res1 = re.findall(pat, inp)

    # Add the found tags to the set to ensure uniqueness
    for data in res1:
        res.add(data)

# Print the unique tags in sorted, semicolon-separated format
print(';'.join(sorted(list(res))))

'''Explanation:

> Define Regular Expression Pattern:
pat = r'<([a-z0-9]+)': Defines a regular expression pattern to match HTML or XML-like tags. 
It captures the tag names, allowing alphanumeric characters for tags.

> Read the Number of Lines (n):
n = int(input()): Reads the number of lines to process.

> Initialize a Set (res) to Store Unique Tags:
res = set(): Initializes an empty set to store unique tags.

> Loop Through Each Line of Input:
for _ in range(n):: Iterates through each line of input.

> Find Tags Using Regular Expression (re.findall):
res1 = re.findall(pat, inp): Uses re.findall to find all matches of the pattern in the current line of input (inp).
The matches are tag names, and they are stored in the list res1.

> Add Tags to the Set (res) for Uniqueness:
for data in res1: res.add(data): Adds each tag found in the current line to the set (res) to ensure uniqueness.
Print Unique Tags in Sorted, Semicolon-Separated Format:

print(';'.join(sorted(list(res)))): Converts the set to a sorted list, joins the list elements with semicolons, and prints the result.
The script effectively collects unique tags from the input lines and prints them in a sorted, semicolon-separated format.'''