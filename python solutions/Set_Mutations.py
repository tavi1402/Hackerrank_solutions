'''this code reads a set SET_A, performs a series of operations on it (e.g., union, intersection, difference), 
and prints the sum of the elements in the final set SET_A. The code uses the eval() function to execute 
operations dynamically based on user input.'''
# Read an integer 'A' from the standard input
A = int(input())

# Read a space-separated list of integers and create a set 'SET_A' from it
SET_A = set(map(int, input().split()))

# Read an integer 'N' from the standard input
N = int(input())

# Loop 'N' times to perform a series of operations
for _ in range(N):
    # Read a line and split it into a list of strings
    operation = input().split()
    
    # Read a space-separated list of integers and create a new set 'new_set'
    new_set = set(map(int, input().split()))
    
    # Execute the operation on 'SET_A' using eval, with the operation and new_set
    eval('SET_A.{}({})'.format(operation[0], new_set))

# Print the sum of the elements in the final 'SET_A'
print(sum(SET_A))
