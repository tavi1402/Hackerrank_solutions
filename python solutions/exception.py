'''this code handles integer division for multiple test cases, catching and printing an error message if an exception 
occurs during the division. The use of try and except allows the code to continue processing other test cases even if 
an error occurs for one of them.'''

# Read an integer T representing the number of test cases.
T = int(input())

# Iterate through each test case.
for i in range(T):
    try:
        # Try to read two integers a and b from the user.
        a, b = map(int, input().split())
        
        # Perform integer division and print the result.
        print(a // b)
    except Exception as e:
        # If an exception occurs during division, print an error message.
        print("Error Code:", e)
