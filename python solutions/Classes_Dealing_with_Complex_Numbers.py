'''This code defines a class for complex numbers and provides various operations like addition, subtraction, 
multiplication, division, magnitude calculation, and customized string representation for complex numbers. 
It reads two complex numbers from the user, performs these operations, and prints the results.'''

import math

# Define a class called 'Complex' to represent complex numbers.
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real  # Initialize the real part of the complex number.
        self.imaginary = imaginary  # Initialize the imaginary part of the complex number.

    def __add__(self, no):
        # Override the addition operation to add two complex numbers.
        return Complex((self.real + no.real), self.imaginary + no.imaginary)

    def __sub__(self, no):
        # Override the subtraction operation to subtract one complex number from another.
        return Complex((self.real - no.real), self.imaginary - no.imaginary)

    def __mul__(self, no):
        # Override the multiplication operation to multiply two complex numbers.
        r = (self.real * no.real) - (self.imaginary * no.imaginary)
        i = (self.real * no.imaginary + no.real * self.imaginary)
        return Complex(r, i)

    def __truediv__(self, no):
        # Override the division operation to divide two complex numbers.
        # It also calculates the conjugate of the denominator to perform the division.
        conjugate = Complex(no.real, (-no.imaginary))
        num = self * conjugate
        denom = no * conjugate
        try:
            # Attempt to perform the division and return the result.
            return Complex((num.real / denom.real), (num.imaginary / denom.real))
        except Exception as e:
            # Handle exceptions (e.g., division by zero) and print an error message.
            print(e)

    def mod(self):
        # Calculate the magnitude (modulus) of the complex number.
        m = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(m, 0)

    def __str__(self):
        # Customize the string representation of the complex number.
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    # Read two sets of float values from the user, each representing a complex number.
    c = map(float, input().split())
    d = map(float, input().split())
    
    # Create two Complex objects 'x' and 'y' with the provided input values.
    x = Complex(*c)
    y = Complex(*d)
    
    # Print the results of various operations on the complex numbers in a formatted way.
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
