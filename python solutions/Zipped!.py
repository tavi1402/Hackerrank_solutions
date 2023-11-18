'''this code takes input data representing the scores of N students in X subjects, calculates the average score for 
each subject, and prints the results. The zip(*io) expression is used to transpose the matrix, allowing the code to 
iterate over the columns, and the average of each column is printed.'''

# Read N (number of students) and X (number of subjects) from the user.
N, X = input().split()

# Create an empty list 'io' to store the input data.
io = list()

# Read X lines of input, each representing the scores of N students in a subject.
for _ in range(int(X)):
    # Read the input line, convert it to a list of floats, and append it to the 'io' list.
    ip = map(float, input().split())
    io.append(ip)

# Use the zip function to iterate over the columns of the 'io' list.
for i in zip(*io):
    # Calculate the average of each column and print the result.
    print(sum(i) / len(i))
