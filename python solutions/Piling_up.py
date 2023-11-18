'''This code arranges cubes by picking them from the left or right, but the top cube must be smaller than the one below. 
It does this for different sets of cubes and says if it's possible (Yes) or not (No). 
It uses a list to remember the answers and checks the sizes of cubes to make the decision.'''
# Initialize an empty list to store the results
ANS = []

# Read the number of test cases from the user
t = int(input())

# Loop through each test case
for _ in range(t):
    # Read the number of cubes in the test case
    n = int(input())

    # Read the lengths of the cubes and store them in a list
    s1 = list(map(int, input().split()))

    # Loop through all but the last cube
    for _ in range(n-1):
        # Check if the leftmost cube is greater than or equal to the rightmost cube
        if s1[0] >= s1[len(s1)-1]:
            a = s1[0]  # Store the value of the leftmost cube
            s1.pop(0)  # Remove the leftmost cube from the list
        # If the leftmost cube is smaller than the rightmost cube
        elif s1[0] < s1[len(s1)-1]:
            a = s1[len(s1)-1]  # Store the value of the rightmost cube
            s1.pop(len(s1)-1)  # Remove the rightmost cube from the list
        else:
            pass  # Do nothing if both cubes are of the same size

        # Check if there is only one cube left, and if so, append "Yes" to the result list
        if len(s1) == 1:
            ANS.append("Yes")
        # Check if the current cube is larger than the stored value 'a', or if the last cube is larger
        elif (s1[0] > a) or (s1[len(s1)-1] > a):
            ANS.append("No")  # If either condition is met, append "No" and break out of the loop
            break

# Print the results for all test cases, each on a new line
print("\n".join(ANS))
