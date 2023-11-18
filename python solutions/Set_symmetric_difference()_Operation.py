'''this code reads two sets of integers, calculates the symmetric difference (elements that are unique to each set), 
and prints the number of unique elements in the symmetric difference set. The leading underscores _ are used 
to ignore values that are read from the input but not used in the code.'''
# Read and ignore an integer (no longer needed) from the standard input
_ = int(input())

# Read a space-separated list of integers and create a set 'SET_N' from it
SET_N = set(map(int, input().split()))

# Read and ignore another integer (no longer needed) from the standard input
_ = int(input())

# Read a space-separated list of integers and create a set 'SET_B' from it
SET_B = set(map(int, input().split()))

# Calculate the symmetric difference between 'SET_N' and 'SET_B', which contains elements
# that are unique to each set (i.e., elements that are in one set but not the other)
symmetric_difference = SET_N.symmetric_difference(SET_B)

# Print the length of the symmetric difference (number of unique elements)
print(len(symmetric_difference))
