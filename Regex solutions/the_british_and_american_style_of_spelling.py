'''What we're doing in this code: 
this script reads a series of lines, consolidates them into a string s, and then searches for occurrences of 
specified patterns (and their modified versions) in this consolidated string. The count of matches for each 
pattern is printed. The modification of the pattern involves removing the last two characters and appending 
"se". The specific behavior and purpose may depend on the context of the problem being solved.
'''

import re

# Read the number of lines to process and build the string
s = ""
for _ in range(int(input())):
    s = s + " " + input()
s = s.strip()

# Read the number of patterns to search for
for _ in range(int(input())):
    a = input()
    # Count the occurrences of the pattern and its modified version in the consolidated string
    print(len(re.findall(r'{}|{}'.format(a, a[:-2] + "se"), s)))
