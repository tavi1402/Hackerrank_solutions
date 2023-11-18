'''this code evaluates a mathematical expression provided as a string and checks if the result is equal to a given 
integer k. The outcome (True or False) is then printed to the standard output.'''

# Check if the script is being run as the main module.
if __name__ == "__main__":
    # Read integers x and k from the user.
    x, k = map(int, input().strip().split())
    
    # Read a string from the user.
    string = input().strip()

    # Evaluate the string as a mathematical expression and check if it is equal to k.
    if eval(string) == k:
        # If the result is equal to k, print True.
        print(True)
    else:
        # If the result is not equal to k, print False.
        print(False)
