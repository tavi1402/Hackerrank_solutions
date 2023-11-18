'''This code is a Python program that calculates and prints the angle between two vectors in 3D space. 
It defines a `Points` class to represent 3D points and implements methods for vector operations, including subtraction, 
dot product, cross product, and vector magnitude. The program reads four sets of 3D coordinates from the user, creates 
`Points` objects for these coordinates, calculates two vectors, and then determines the angle between these vectors using 
mathematical operations. The final result, which is the angle in degrees, is printed with two decimal places. In essence, 
the code computes the angle between two vectors formed by four 3D points and provides the result in a human-readable 
format.'''

import math  # Import the math module for mathematical functions.

# Define a class called 'Points' to represent 3D points.
class Points(object):
    def __init__(self, x, y, z):
        self.x = x  # Initialize the 'x' coordinate of the point.
        self.y = y  # Initialize the 'y' coordinate of the point.
        self.z = z  # Initialize the 'z' coordinate of the point.

    def __sub__(self, no):
        # Override the subtraction operation to subtract one point from another, returning a new point.
        return Points((self.x - no.x), (self.y - no.y), (self.z - no.z))

    def dot(self, no):
        # Calculate the dot product of two points (vectors).
        return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)

    def cross(self, no):
        # Calculate the cross product of two points (vectors).
        return Points((self.y * no.z - self.z * no.y), (self.z * no.x - self.x * no.z), (self.x * no.y - self.y * no.x))

    def absolute(self):
        # Calculate the magnitude (length) of the point (vector).
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

# Check if the script is run as the main program (not imported as a module).
if __name__ == '__main__':
    points = list()  # Create an empty list to store four sets of 3D coordinates.

    # Read input from the user for four 3D points and append them to the 'points' list.
    for i in range(4):
        a = list(map(float, input().split()))  # Read a line of input and split it into a list of floats.
        points.append(a)  # Append the list of coordinates to the 'points' list.

    # Create 'Points' objects a, b, c, and d using the coordinates from 'points' list.
    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])

    # Calculate two vectors 'x' and 'y' by taking the cross product of vector pairs (b - a) and (c - b), and (c - b) and (d - c).
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)

    # Calculate the angle between vectors 'x' and 'y' using the dot product and vector magnitudes.
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    # Print the angle in degrees with two decimal places using the 'math.degrees' function and format specifier '%.2f'.
    print("%.2f" % math.degrees(angle))
