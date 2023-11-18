def merge_the_tools(string, k):
    # Create an empty list to store characters of the current substring
    temp = []
    len_temp = 0
    for item in string:
        # Increment the length of the current substring
        len_temp += 1
        # If the current character is not already in the substring (temp), add it
        if item not in temp:
            temp.append(item)
        # If the current substring has reached the desired length (k)
        if len_temp == k:
            # Print the modified substring without duplicate characters
            print(''.join(temp))
            # Reset the temporary list and length counter for the next substring
            temp = []
            len_temp = 0

if __name__ == '__main':
    # Input the string and value of k
    string, k = input(), int(input())
    # Call the merge_the_tools function with the provided inputs
    merge_the_tools(string, k)
