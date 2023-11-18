'''this code calculates the happiness by checking how many integers from the array are present in the "good" set 
and subtracting the count of integers present in the "bad" set. The final result is printed to the standard output.'''

# Check if the script is being run as the main module.
if __name__ == "__main__":
    # Initialize happiness to 0.
    happiness = 0

    # Read integers n and m from the user.
    n, m = map(int, input().strip().split(' '))
    
    # Read an array of integers from the user.
    arr = list(map(int, input().strip().split(' ')))

    # Read sets of "good" and "bad" integers from the user.
    good = set(map(int, input().strip().split(' ')))
    bad = set(map(int, input().strip().split(' ')))

    # Iterate over the array of integers and update the happiness based on the sets.
    for i in arr:
        if i in good:
            happiness += 1
        elif i in bad:
            happiness -= 1

    # Print the final happiness.
    print(happiness)
