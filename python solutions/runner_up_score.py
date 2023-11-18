if __name__ == '__main__':
    n = int(input()) # taking number input.
    arr = map(int, input().split()) # taking array input by taking list of numbers separated by spaces.
    print(sorted(list(set(arr)))[-2])
    
# set(arr) ensures that there are no duplicate elements in the array.
# list(set(arr)) turns this unique list back into a regular list of numbers.
# sorted() converts it into ascending order.
# [-2] means taking second last number because we set it in ascending order and if we want second largest number.