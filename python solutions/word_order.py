from collections import Counter

# Read the number of input lines
n = int(input())

# Initialize an empty list to store the input data
list1 = []

# Read input lines and split them into lists of elements
for _ in range(n):
    input_line = input().split()  # Read a line and split it into elements
    list1.append(input_line)  # Append the list of elements to list1

# Flatten the list of lists into a single list
flat_list1 = [item for sublist in list1 for item in sublist]

# Create a Counter object to count element occurrences
result = Counter(flat_list1)

# Print the number of distinct elements
print(len(result))

# Print the counts of each element
print(*result.values())
