'''this code reads two sets of integers, calculates the intersection (common elements) between these sets, 
and prints the number of common elements in the sets 'SET_N' and 'SET_B'. The leading underscores _ are used 
to ignore values that are read from the input but not used in the code.'''
# Read and ignore an integer (no longer needed) from the standard input
_ = int(input())

# Read a space-separated list of integers and create a set 'SET_N' from it
SET_N = set(map(int, input().split()))

# Read and ignore another integer (no longer needed) from the standard input
_ = int(input())

# Read a space-separated list of integers and create a set 'SET_B' from it
SET_B = set(map(int, input().split()))

# Calculate the intersection of 'SET_N' and 'SET_B', which contains common elements
# and print the number of elements in the intersection
print(len(SET_N & SET_B))
