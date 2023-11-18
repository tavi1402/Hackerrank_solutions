# Read the number of elements in the tuple
n = int(input())

# Read the space-separated integers and create a tuple
integer_list = tuple(map(int, input().split()))

# Calculate the hash value for the tuple
hash_value = hash(integer_list)

# Print the result of the hash calculation
print(hash_value)
