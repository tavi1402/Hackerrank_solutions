'''this code takes input to create a set of integers, performs various operations on the set 
(e.g., popping, removing, discarding elements), and then calculates and prints the sum of the remaining 
elements in the set.'''
# Read an integer 'n' from the standard input
n = int(input())

# Read a space-separated list of integers and create a set 's' from it
s = set(map(int, input().split()))

# Iterate 'n' times, where 'n' is the number of operations to be performed
for i in range(int(input())):
    # Read a line and split it into a list of strings
    s1 = input().split()

    # Check the operation indicated by the first element of the list
    if s1[0] == 'pop':
        # If it's 'pop', remove and return an arbitrary element from the set
        s.pop()
    elif s1[0] == 'remove':
        # If it's 'remove', remove the specified integer from the set
        s.remove(int(s1[1]))
    elif s1[0] == 'discard':
        # If it's 'discard', remove the specified integer from the set (if present)
        s.discard(int(s1[1]))

# Calculate and print the sum of the remaining elements in the set 's'
print(sum(s))
