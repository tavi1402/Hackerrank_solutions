import re  # Import the regular expression module

# Define a string containing programming languages separated by colons
s1 = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA: ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART: GROOVY:OBJECTIVEC"

# Use re.split to split the string into a list of programming languages
sl = re.split(r'\W', s1)

# Filter out empty strings from the list
sl = [i for i in sl if i != ""]

# Loop through each test case
for _ in range(int(input())):
    # Read a line of input containing programming languages
    if any(map(lambda x: x in sl, input().split())):
        print("VALID")  # If any language is valid, print "VALID"
    else:
        print("INVALID")  # If none of the languages are valid, print "INVALID"
