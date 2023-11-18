'''The pattern generates a series of numbers where each number is formed by repeating the digit 'i' 'i' times. 
For example, when i is 1, it generates the series: 1, 22, 333, 4444, and so on. The code uses integer division // 
to ensure that the result is an integer.'''
# Read an integer from the standard input
n = int(input())

# Loop from 1 to n-1
for i in range(1, n):
    # Calculate and print the i-th number in the pattern
    print((10**(i) // 9) * i)
