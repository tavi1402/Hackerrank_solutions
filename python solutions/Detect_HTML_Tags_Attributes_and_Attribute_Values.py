'''The code extracts and prints the HTML tags and their attributes from the input HTML content.'''

from html.parser import HTMLParser

# Define a custom HTMLParser class by subclassing HTMLParser.
class MyHTMLParser(HTMLParser):
    # Override the handle_starttag method to handle the start tags of HTML elements.
    def handle_starttag(self, tag, attrs):
        print(tag)  # Print the name of the HTML element (tag).
        # For each attribute in the tag, print the attribute name and its value.
        [print('-> {} > {}'.format(*attr)) for attr in attrs]

# Read the number of lines of HTML content from the user as input.
html = '\n'.join([input() for _ in range(int(input()))])

# Create an instance of the custom HTMLParser class.
parser = MyHTMLParser()

# Feed the HTML content to the parser for parsing.
parser.feed(html)

# Close the parser to finish parsing.
parser.close()
