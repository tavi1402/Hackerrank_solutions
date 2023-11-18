'''This code takes an input string, sorts its characters alphabetically, and then uses a Counter 
to count the frequency of each character. It then prints the three most common characters and their counts.'''
# Import the Counter class from the collections module
from collections import Counter

# Read a string input from the user
s = input()

# Sort the characters in the input string alphabetically
s = sorted(s)

# Create a Counter object to count the frequency of each character in the sorted string
freq = Counter(list(s))

# Loop through the three most common elements and their counts
for i, j in freq.most_common(3):
    # 'i' represents the character, and 'j' represents its count
    print(i, j)
