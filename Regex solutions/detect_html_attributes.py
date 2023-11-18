'''The provided Python code processes input elements that represent HTML or XML-like tags, 
extracts information about the tags and their attributes, and then prints the results in a sorted format. 
Here's a breakdown of the code:'''

import re  # Import the regular expression module

res = []  # Initialize an empty list to store results
tag_attr = {}  # Initialize an empty dictionary to store tag attributes

# Loop through each test case (number of elements)
for _ in range(int(input())):
    element = input()  # Read an input element containing HTML-like tags
    tags = re.findall(r"(?<=\<)\w+", element)  # Find all tags in the element # Extracting Tags

    # Loop through each tag
    for tag in tags:
        # Check if the tag has attributes using a regular expression
        if (attrs := re.search(fr"<\b{tag}\b([^>]+)>", element)) is not None: # Extracting Tag Attributes
            # Extract individual attribute names using regular expression
            each_attr = re.findall(r"((?<=\s)\w+)=", attrs.group()) # Extracting Attribute Names
            # Update the dictionary with the attributes for the current tag
            tag_attr[tag] = list(set(each_attr + tag_attr.get(tag, [])))
        else:
            # If the tag has no attributes, update the dictionary with an empty attribute list
            tag_attr[tag] = list(set([""] + tag_attr.get(tag, [])))

# Iterate through the tag_attr dictionary and format the results
[res.append(f"{tag}:{','.join(sorted(attr))}") for tag, attr in tag_attr.items()]

# Print the sorted results
print(*sorted(res), sep="\n")

'''
1. Extracting Tags:

> tags = re.findall(r"(?<=\<)\w+", element)

- (?<=\<): Positive lookbehind assertion, asserts that what immediately precedes the current position in the string is a < character.
- \w+: Matches one or more word characters (alphanumeric or underscore). This captures the tag name.
- Overall, this regex captures the tag names in the HTML-like element.

2. Extracting Tag Attributes:

> if (attrs := re.search(fr"<\b{tag}\b([^>]+)>", element)) is not None:

- <\b{tag}\b: Matches the literal <, the tag name (with word boundaries \b for exact matching), and another literal >.
- ([^>]+): Capturing group that matches one or more characters (except >) inside the tag. This captures the entire attribute portion.
- The entire regex captures the tag and its attributes.

3. Extracting Attribute Names:

> each_attr = re.findall(r"((?<=\s)\w+)=", attrs.group())

- ((?<=\s)\w+): Capturing group that matches one or more word characters (\w+) preceded by a whitespace character ((?<=\s)). This captures attribute names.
- =: Matches the equal sign that separates the attribute name and value.
- This regex captures attribute names within the attribute portion.
'''