'''this code calculates the symmetric difference of two sets of integers, sorts the result, and prints the elements 
that are in either set_m or set_n but not both. The symmetric difference is obtained using the ^ (caret) operator.'''

# Check if the script is being run as the main module.
if __name__ == "__main__":
    # Read an integer M and a set of integers set_m from the user.
    M = int(input().strip())
    set_m = set(map(int, input().strip().split(' ')))
    
    # Read an integer N and a set of integers set_n from the user.
    N = int(input().strip())
    set_n = set(map(int, input().strip().split(' ')))
    
    # Calculate the symmetric difference of set_m and set_n, and print the sorted result.
    for j in sorted(set_m ^ set_n):
        print(j)
