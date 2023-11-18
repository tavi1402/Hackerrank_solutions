'''The code sorts a list of people's data based on the integer value of the third element (presumably age) and 
then formats their names using the name_format function. The decorator person_lister is used to sort the list and 
format the names before printing them. The resulting names are prefixed with "Mr." for males and "Ms." for females.'''

import operator

# Define a decorator function 'person_lister' that takes another function 'func' as an argument.
def person_lister(func):
    # Define an inner function 'inner' that takes a list of 'people' as an argument.
    def inner(people):
        # Sort the 'people' list based on the integer value of the third element of each person's data.
        # The lambda function extracts and converts the third element to an integer for sorting.
        sorted_people = sorted(people, key=lambda x: int(x[2]))

        # Apply the 'func' function to each person in the sorted list and create a new list.
        # This new list contains formatted names based on the 'func' function's logic.
        formatted_names = [func(p) for p in sorted_people]

        return formatted_names  # Return the list of formatted names.

    return inner  # Return the 'inner' function as the result of the 'person_lister' decorator.

# Define a function 'name_format' that takes a 'person' as an argument.
# This function formats the name based on the gender ('M' or 'F') of the person.
def name_format(person):
    # If the person is male ('M'), prefix the name with "Mr.".
    # If the person is female ('F'), prefix the name with "Ms.".
    # Then, add the first name and last name separated by a space.
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    # Read an integer from the user, indicating the number of people's data to input.
    num_people = int(input())
    
    # Read and split the data for each person, creating a list of lists 'people'.
    people = [input().split() for i in range(num_people)]

    # Call the 'name_format' function, which is decorated by 'person_lister'.
    # This will sort and format the people's names based on the decorator's logic.
    formatted_names = name_format(people)

    # Print the formatted names, separating them by newline characters.
    print(*formatted_names, sep='\n')
