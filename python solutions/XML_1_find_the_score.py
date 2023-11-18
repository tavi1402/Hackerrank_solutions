'''this code calculates the total number of attributes in an XML tree by parsing the XML document using ElementTree. 
The result is then printed to the standard output.'''

import sys
import xml.etree.ElementTree as etree

# Define a function 'get_attr_number' to calculate the total number of attributes in an XML tree.
def get_attr_number(node):
    # Return the sum of the number of attributes in the current node and its children.
    return len(node.attrib) + sum(get_attr_number(child) for child in node)

if __name__ == '__main__':
    # Read a line from the standard input (not used in the code).
    sys.stdin.readline()
    
    # Read the XML document from the standard input.
    xml = sys.stdin.read()
    
    # Parse the XML document using ElementTree and create an ElementTree object 'tree'.
    tree = etree.ElementTree(etree.fromstring(xml))
    
    # Get the root of the XML tree.
    root = tree.getroot()
    
    # Call the 'get_attr_number' function on the root of the XML tree and print the result.
    print(get_attr_number(root))
