'''this code calculates and prints the cube of the first n numbers in the Fibonacci sequence using a 
generator function and a lambda function.'''

# Define a lambda function 'cube' that calculates the cube of a number 'x'.
cube = lambda x: x ** 3

# Define a generator function 'fibonacci' that yields the first 'n' numbers of the Fibonacci sequence.
def fibonacci(n):
    a, b, c = 0, 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    # Read an integer 'n' from the user.
    n = int(input())

    # Generate the first 'n' Fibonacci numbers using the 'fibonacci' generator function,
    # apply the 'cube' function to each number using 'map', and convert the result to a list.
    result = list(map(cube, fibonacci(n)))

    # Print the list of cubed Fibonacci numbers.
    print(result)
