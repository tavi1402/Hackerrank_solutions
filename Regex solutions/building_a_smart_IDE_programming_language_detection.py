import re  # Import the regular expression module
import sys  # Import the sys module for reading from stdin

# Read the entire input from stdin
code = sys.stdin.read()

# Check if the C language code is present
if re.search("#include<stdio.h>", code) is not None:
    print("C")
# Check if the Java language code is present
elif re.search("import java.io", code) is not None:
    print("Java")
# If neither C nor Java patterns are found, assume it's Python
else:
    print("Python")
