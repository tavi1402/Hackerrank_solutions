'''This code calculates the angle MBC in degrees and prints it with the degree symbol.'''

import math

# Read the lengths of sides AB and BC from the user.
ab = int(input())
bc = int(input())

# Calculate the length of side CA using the Pythagorean theorem (hypotenuse).
ca = math.hypot(ab, bc)

# Calculate the length of median MC, which is half of CA.
mc = ca / 2

# Calculate the angle BCA using the arcsine function (inverse sine).
bca = math.asin(ab / ca)

# Calculate the length of BM using the law of cosines.
bm = math.sqrt((bc**2 + mc**2) - (2 * bc * mc * math.cos(bca)))

# Calculate the angle MBC using the law of sines.
mbc = math.asin(math.sin(bca) * mc / bm)

# Convert the angle from radians to degrees and round it to the nearest integer.
angle_in_degrees = int(round(math.degrees(mbc)))

# Print the angle in degrees with the degree symbol (°).
print(angle_in_degrees, '\u00B0', sep='')
