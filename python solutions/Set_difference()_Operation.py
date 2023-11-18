''' this code reads two sets of integers, calculates the difference (elements in SET_N but not in SET_B), 
and prints the number of unique elements in the resulting set NEW_SET. The leading underscores _ are used 
to ignore values that are read from the input but not used in the code.'''
# Read and ignore an integer (no longer needed) from the standard input
_ = int(input())

# Read a space-separated list of integers and create a set 'SET_N' from it
SET_N = set(map(int, input().split()))

# Read and ignore another integer (no longer needed) from the standard input
_ = int(input())

# Read a space-separated list of integers and create a set 'SET_B' from it
SET_B = set(map(int, input().split()))

# Create a new set 'NEW_SET' by taking the difference of 'SET_N' and 'SET_B'
# This will contain elements that are in 'SET_N' but not in 'SET_B'
NEW_SET = SET_N.difference(SET_B)

# Print the length of the 'NEW_SET' (number of unique elements)
print(len(NEW_SET))
