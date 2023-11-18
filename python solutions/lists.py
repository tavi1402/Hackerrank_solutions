'''Consider a list (list = []). You can perform the following commands:

- insert i e: Insert integer e at position i.
- print: Print the list.
- remove e: Delete the first occurrence of integer e.
- append e: Insert integer e at the end of the list.
- sort: Sort the list.
- pop: Pop the last element from the list.
- reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command 
will be of the 7 types listed above. Iterate through each command in order and perform the corresponding 
operation on your list.'''

# Get an integer as input from the user and store it in the variable 'num'.
num = int(input())
    
# Create an empty list called 'list' to store elements.
list = []

    # Start a loop that will run 'num' times, based on the integer entered by the user.
for i in range(0, num):
        # Get a command as input from the user and split it into a list using spaces, then store it in the 'command' variable.
        n = input().split()

        # Check the first element of the 'command' list to determine the action to be taken.
        if n[0] == "insert":
            # If the command is "insert," insert an element at a specified position in the list.
            list.insert(int(n[1]), int(n[2]))
        elif n[0] == "append":
            # If the command is "append," add an element to the end of the list.
            list.append(int(n[1]))
        elif n[0] == "pop":
            # If the command is "pop," remove and return the last element from the list.
            list.pop()
        elif n[0] == "print":
            # If the command is "print," display the current contents of the list.
            print(list)
        elif n[0] == "remove":
            # If the command is "remove," remove the first occurrence of a specified element from the list.
            list.remove(int(n[1]))
        elif n[0] == "sort":
            # If the command is "sort," sort the elements in the list in ascending order.
            list.sort()
        else:
            # If none of the above commands match, reverse the elements in the list.
            list.reverse()
