# # Enter key-value pairs separated by spaces
# data = {key: value for key, value in input("Enter key-value pairs separated by spaces: ").split()}

data = {}
while True:
    key = input("Enter a key (or press Enter to finish): ")
    if not key:
        break  # Stop input if Enter key is pressed
    value = input("Enter the corresponding value: ")
    data[key] = value

print(data)