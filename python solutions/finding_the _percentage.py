# If this script is executed as the main program:
if __name__ == '__main__':
    # Read an integer 'n' from the user, representing the number of students.
    n = int(input())
    
    # Create an empty dictionary 'student_marks' to store student names and their scores.
    student_marks = {}

    # Loop 'n' times to input student names and their space-separated scores.
    for _ in range(n):
        # Read two values from a line: student's name and a space-separated string of scores.
        name, line = input().split()

        # Convert the space-separated scores into a list of floating-point numbers.
        scores = list(map(float, line))

        # Store the student's name as the key and their scores list as the value in the dictionary.
        student_marks[name] = scores

    # Read the name of the student whose average score you want to calculate.
    query_name = input()

# Get the list of scores for the student with the name 'query_name'.
output = list(student_marks[query_name])

# Calculate the average (mean) score for the student.
per = sum(output) / len(output)

# Print the average score with exactly two decimal places.
print("%.2f" % per)
