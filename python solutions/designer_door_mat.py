# it excepts two space separated integers N represents the number of rows, and M represents the width of the output.
N, M = map(int, input().split())
# loop to iterate through a range of values starting from 1 to N(exclusive) with a step of 2
for i in range(1, N, 2):
    # in this loop ".|." is printed through i iterations and with the empty spaces are filled with "-"
    print((i * ".|.").center(M,"-"))
# after the first loop WELCOME is printed within a string of width M where the remaining spaces are filled with "-"
print("WELCOME".center(M, "-"))
# this loop iterates through a range of values starting from N-2 (the second-to-last row) 
# down to -1 (inclusive) with a step of -2. It means it will loop through the even numbers (in reverse order).
for i in range(N-2, -1, -2):
    # similar to line 6 printing the same pattern but with even numbers of repititions, creating a mirrored pattern
    print((i * ".|.").center(M, "-"))  