'''this code defines a custom HTML parser class and uses it to parse HTML-like tags. 
It prints the tag names, attributes, and whether the tags are start, end, or empty (self-closing) tags for 
each line of input.'''

from html.parser import HTMLParser

# Define a custom HTML parser class
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ('Start :', tag)
        for ele in attrs:
            print ('->', ele[0], '>', ele[1])
    
    def handle_endtag(self, tag):
        print ('End   :', tag)
    
    def handle_startendtag(self, tag, attrs):
        print ('Empty :', tag)
        for ele in attrs:
            print ('->', ele[0], '>', ele[1])

# Create an instance of the custom HTML parser
parser = MyHTMLParser()

# Read the number of lines to parse
for _ in range(int(input())):
    # Parse each line using the custom parser
    parser.feed(input())
