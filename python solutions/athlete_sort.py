'''this code takes input of rows and columns, sorts the rows based on the specified column index K, and then prints 
the sorted rows. The sorting is done using the sorted() function with a lambda function as the key to extract the value 
from the specified column for comparison.'''

# Import necessary modules.
import math
import os
import random
import re
import sys

# Read N (number of rows) and M (number of columns) from the user.
N, M = map(int, input().split())

# Read the rows of data from the user and store them in a list.
rows = [input() for _ in range(N)]

# Read K (the column index to sort by) from the user.
K = int(input())

# Sort the rows based on the specified column index K using a lambda function as the key.
for row in sorted(rows, key=lambda row: int(row.split()[K])):
    # Print each row after sorting.
    print(row)
