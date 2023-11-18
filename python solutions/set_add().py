# Read an integer 'n' from the standard input (STDIN)
n = int(input())

# Initialize an empty set 'NAMES' to store unique names
NAMES = set([])

# Use a loop to input names and add them to the 'NAMES' set
for i in range(n):
    # Read a name from the standard input (STDIN)
    name = input()
    # Add the name to the 'NAMES' set, which automatically ensures uniqueness
    NAMES.add(name)

# Print the number of unique names
print(len(NAMES))
