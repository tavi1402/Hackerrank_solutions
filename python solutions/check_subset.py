'''In each iteration of the loop, it reads two sets, set_a and set_b, and checks if set_a is a subset of set_b. 
If the result of the set difference (set_a - set_b) is an empty set, it means that all elements in set_a are also 
in set_b, making set_a a subset of set_b. It prints "True" in this case. Otherwise, it prints "False."'''
# Loop for the number of test cases
for i in range(int(input())):
    # Read the number of elements in the first set and the set itself
    a = int(input())
    set_a = set(map(int, input().split()))

    # Read the number of elements in the second set and the set itself
    b = int(input())
    set_b = set(map(int, input().split()))

    # Check if set_a is a subset of set_b
    if len(set_a - set_b) == 0:
        print("True")
    else:
        print("False")
