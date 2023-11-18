'''this code calculates the average of unique elements in a list of integers and prints the result to the standard output.
 The use of a set ensures that duplicate elements are removed before calculating the average.'''

# Define a function 'average' that takes a list of integers 'array'.
def average(array):
    # Convert the list to a set to remove duplicate elements.
    array = set(array)
    # Calculate the average of the elements in the set and return the result.
    return sum(array) / len(array)

if __name__ == '__main__':
    # Read an integer 'n' from the user, indicating the number of elements in the list.
    n = int(input())
    
    # Read a list of integers 'arr' from the user.
    arr = list(map(int, input().split()))
    
    # Call the 'average' function with the list 'arr' and store the result in 'result'.
    result = average(arr)
    
    # Print the result (average of unique elements in the list).
    print(result)
