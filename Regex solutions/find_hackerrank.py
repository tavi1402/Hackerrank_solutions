import re  # Import the regular expression module

# Loop through the number of test cases specified by the user
for _ in range(int(input())):
    # Read each line of input as a conversation
    conversation = input()
    
    # Check if the conversation starts and ends with "hackerrank"
    if re.search(r"\Ahackerrank\Z", conversation) is not None:
        print("0")  # If yes, print "0"
    # Check if the conversation starts with "hackerrank"
    elif re.search(r"\Ahackerrank", conversation) is not None:
        print("1")  # If yes, print "1"
    # Check if the conversation ends with "hackerrank"
    elif re.search(r"hackerrank\Z", conversation) is not None:
        print("2")  # If yes, print "2"
    else:
        print("-1")  # If none of the above conditions are met, print "-1"
