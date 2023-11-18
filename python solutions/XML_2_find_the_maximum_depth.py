'''this code calculates the maximum depth of an XML tree by parsing the XML document using the ElementTree module. 
The result is then printed to the standard output.'''

# Import the ElementTree module from xml.etree.
import xml.etree.ElementTree as etree

# Initialize the global variable maxdepth to 0.
maxdepth = 0

# Define a function 'depth' to calculate the maximum depth of the XML tree.
def depth(elem, level):
    global maxdepth
    # If the current level is equal to the current maximum depth, increment maxdepth.
    if (level == maxdepth):
        maxdepth += 1
    # Recursively iterate over the children of the current element and update the level.
    for child in elem:
        depth(child, level + 1)

if __name__ == '__main__':
    # Read an integer 'n' from the user, indicating the number of lines in the XML document.
    n = int(input())
    
    # Initialize an empty string 'xml' to store the XML document.
    xml = ""
    
    # Read 'n' lines of the XML document from the user and concatenate them.
    for i in range(n):
        xml = xml + input() + "\n"
    
    # Parse the XML document using ElementTree and create an ElementTree object 'tree'.
    tree = etree.ElementTree(etree.fromstring(xml))
    
    # Call the 'depth' function on the root of the XML tree to calculate the maximum depth.
    depth(tree.getroot(), -1)
    
    # Print the maximum depth of the XML tree.
    print(maxdepth)
