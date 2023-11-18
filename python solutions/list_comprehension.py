if __name__ == '__main__':
    # Read integer inputs from the user and store them in x, y, z, and n
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Initialize an empty list called 'output' to store the results
    output = [
        [i, j, k]  # Create a list containing values i, j, and k
        for i in range(x + 1)  # Iterate i from 0 to x (inclusive)
        for j in range(y + 1)  # Iterate j from 0 to y (inclusive)
        for k in range(z + 1)  # Iterate k from 0 to z (inclusive)
        if i + j + k != n  # Add the list [i, j, k] to 'output' if i + j + k is not equal to n
    ]
    print(output)
''' using brute force we get 
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    output = [];
    abc = [];
    for X in range(x+1):
        for Y in range(y+1):
            for Z in range(z+1):
                if X+Y+Z != n:
                    abc = [X,Y,Z];
                    output.append(abc);
print(output);    
'''


