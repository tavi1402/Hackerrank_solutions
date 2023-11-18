'''this code demonstrates the use of classes to represent even and odd number streams and a function to print the 
next n elements from a given stream. The print_from_stream function is designed to work with the default EvenStream 
or an optional OddStream provided as an argument.'''

# Define the EvenStream class representing a stream of even numbers.
class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

# Define the OddStream class representing a stream of odd numbers.
class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

# Define the print_from_stream function that prints the next 'n' elements from a given stream.
def print_from_stream(n, stream=EvenStream()):
    # Reset the stream to its initial state.
    stream.__init__()

    # Print the next 'n' elements from the stream.
    for _ in range(n):
        print(stream.get_next())

# Read the number of queries from the user.
queries = int(input())

# Process each query.
for _ in range(queries):
    # Read the stream name and the number of elements 'n' from the user.
    stream_name, n = input().split()
    n = int(n)

    # Check the stream name and call the print_from_stream function accordingly.
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
