# Define a function named 'mutate_string' that takes three arguments: a string 'string', an integer 'position', and a character 'character'
def mutate_string(string, position, character):
    # Convert the input string 'string' into a list of characters 'n'
    n = list(string)
    
    # Replace the character at the specified 'position' in the list 'n' with the new 'character'
    n[position] = character
    
    # Convert the modified list 'n' back into a string and update the 'string' variable with this new value
    string = "".join(n)
    
    # Return the updated 'string' with the character at the specified position changed
    return string

# If this script is executed as the main program:
if __name__ == '__main__':
    # Read a string 's' from the user
    s = input()
    
    # Read two values (an integer 'i' and a character 'c') from the user, separated by a space
    i, c = input().split()
    
    # Call the 'mutate_string' function with the input string 's', integer 'i', and character 'c'
    s_new = mutate_string(s, int(i), c)
    
    # Print the updated string 's_new' with the character at the specified position changed
    print(s_new)
