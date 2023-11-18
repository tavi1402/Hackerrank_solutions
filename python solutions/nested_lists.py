Result =[] # empty list for collecting result
scorelist = [] # empty list to keep the track of scores

if __name__ == '__main__': # starting the main program
    n = int(input())
    while range (n): # input number and repeat the loop that many times
        name = input() # input for name
        score = float(input()) # input for score
        Result += [[name,score]] # it adds name and score as a pair to the result
        scorelist += [score] # adding the score to the scorelist

    b=sorted(list(set(scorelist)))[1] # here b holds the second smallest score
    # set(scorelist) so there are no duplicate values
    # list() turning this unique list into a regular list
    # sorted() arranging from smallest to largest
    # and [1] is for second item from the sorted list as the second smallest score

    # Now, we look at our list of friends and their scores to find friends with the second lowest score ('b').
    for a, c in sorted(Result):  # We go through the list of names and scores.
        if c == b:  # If a friend's score is the same as the second lowest score ('b')...
            print(a)  # ...we say, "You are one of the friends with the second lowest score," and we print their name.