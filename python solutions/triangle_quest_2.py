'''The code produces an output where each line contains the square of the repeating decimal pattern for the 
corresponding number from 1 to the input value.'''

# Read an integer 'n' from the user. This determines how many iterations the loop will run.
n = int(input())

# Iterate from 1 to 'n' (inclusive) using a for loop.
for i in range(1, n + 1):
    # Inside the loop, calculate and print the result for each iteration.

    # Calculate 10^i using the exponentiation operator '**'. This represents a 1 followed by 'i' number of zeros.
    # For example, if i is 1, this is 10^1 = 10.
    # If i is 2, this is 10^2 = 100, and so on.
    # Then, divide it by 9 to create a number where all the digits are 1, like 1111...1 (i times).

    # Next, square the result using the exponentiation operator '**'. This effectively repeats the pattern of 1's 'i' times.
    # For example, if i is 1, this is (1111...1)^2 = 121.
    # If i is 2, this is (1111...1)^2 = 12321, and so on.

    # Finally, print the result for the current iteration.
    print(((10**i) // 9) ** 2)
