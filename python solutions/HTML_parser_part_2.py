'''this code reads an integer representing the number of lines of HTML content and then reads the HTML content 
line by line. It uses a custom HTML parser to process the HTML content, distinguishing between multi-line and 
single-line comments and data (text). The results are printed to the console.'''

# Import the HTMLParser class from the html.parser module.
from html.parser import HTMLParser

# Define a custom HTML parser class 'MyHTMLParser' that inherits from HTMLParser.
class MyHTMLParser(HTMLParser):
    # Define a method to handle comments in the HTML content.
    def handle_comment(self, comment):
        if '\n' in comment:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')

        print(comment)

    # Define a method to handle data (text) in the HTML content.
    def handle_data(self, data):
        if data == '\n': return  # Skip empty lines.
        print('>>> Data')
        print(data)

html = ""

# Read the number of lines of HTML content from the user.
for i in range(int(input())):
    # Read each line of HTML content, strip trailing whitespaces, and append a newline character.
    html += input().rstrip()
    html += '\n'

# Create an instance of the custom HTML parser 'MyHTMLParser'.
parser = MyHTMLParser()

# Feed the HTML content to the parser for parsing.
parser.feed(html)

# Close the parser to signal the end of input.
parser.close()
