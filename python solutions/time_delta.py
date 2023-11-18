'''
1. It imports necessary modules like math, os, random, re, and sys, although these imports are not used in this code.
2. The time_delta function is defined to calculate the time difference between two timestamps. 
    It uses the datetime module to parse and manipulate the timestamps.
3. The if __name__ == '__main__' block is the main execution part of the script. It reads the number of test cases, 
    reads pairs of timestamps for each test case, calculates the time difference, and writes the results to an output file 
    specified by the 'OUTPUT_PATH' environment variable.
4. The code expects to be run in an environment where the 'OUTPUT_PATH' environment variable is set to specify the 
    output file. It is typically used in a programming competition platform where input and output are predefined.''' 
import os
# Import the 'datetime' module to work with timestamps
from datetime import datetime

# Define the 'time_delta' function to calculate the time difference
def time_delta(t1, t2):
    # Specify the time format for parsing the timestamps
    time_format = '%a %d %b %Y %H:%M:%S %z'
    
    # Parse the input timestamps into 'datetime' objects using the specified format
    t1 = datetime.strptime(t1, time_format)
    t2 = datetime.strptime(t2, time_format)
    
    # Calculate the absolute time difference in seconds and convert it to an integer
    return str(int(abs((t1 - t2).total_seconds())))

# Check if the script is run as the main program
if __name__ == '__main__':
    # Open an output file for writing the results, specified by the 'OUTPUT_PATH' environment variable
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of test cases
    t = int(input())

    # Iterate through each test case
    for t_itr in range(t):
        # Read the two timestamps for each test case
        t1 = input()
        t2 = input()

        # Calculate the time difference using the 'time_delta' function
        delta = time_delta(t1, t2)

        # Write the time difference to the output file
        fptr.write(delta + '\n')

    # Close the output file
    fptr.close()
