'''this code calculates the product of a list of fractions, simplifies the result, 
and then prints it as a tuple of the numerator and denominator.'''

# Import the 'Fraction' class from the 'fractions' module to work with fractions.
from fractions import Fraction

# Import the 'reduce' function from the 'functools' module to calculate the product of fractions.
from functools import reduce

# Define a function 'product' that takes a list of fractions 'fracs'.
def product(fracs):
    # Calculate the product of all fractions in the list using the 'reduce' function.
    # The lambda function 'lambda x, y: x * y' is used to multiply two fractions together.
    t = Fraction(reduce(lambda x, y: x * y, fracs))
    
    # Get the numerator and denominator of the product fraction.
    return t.numerator, t.denominator

if __name__ == '__main__':
    # Read an integer 'n' from the user, indicating the number of fractions.
    n = int(input())

    # Create an empty list 'fracs' to store the fractions.
    fracs = []

    # Read 'n' fractions from the user, split and map the input, and append them to the 'fracs' list.
    for _ in range(n):
        fracs.append(Fraction(*map(int, input().split())))

    # Calculate the product of the fractions using the 'product' function.
    result = product(fracs)

    # Print the simplified result as a tuple (numerator, denominator).
    print(*result)
