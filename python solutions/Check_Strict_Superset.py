'''In this code, it reads the set A and then reads a series of sets, checking if A is a superset of each of them. 
It keeps track of the count of sets where A is a superset (COUNT) and sets where it is not (VALUE). 
If there are any sets for which A is not a superset (VALUE != 0), it prints "False." Otherwise, it prints "True."'''
# Read set 'A' from the standard input and split it into elements
A = set(input().split())

# Initialize counters for 'COUNT' and 'VALUE'
COUNT = 0
VALUE = 0

# Read the number of sets to check against 'A'
for i in range(int(input())):
    # Read a set from the standard input and split it into elements
    set_to_check = set(input().split())

    # Check if 'A' is a superset of 'set_to_check'
    if A.issuperset(set_to_check):
        COUNT += 1
    else:
        VALUE += 1

# Check if any sets were not supersets of 'A'
if VALUE != 0:
    print('False')
else:
    print('True')
