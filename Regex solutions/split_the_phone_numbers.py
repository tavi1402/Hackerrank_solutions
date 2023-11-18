import re  # Import the regular expression module

# Define a regular expression pattern for parsing phone numbers
pattern = re.compile(r'(\d{1,3})[- ](\d{1,3})[- ](\d{4,10})')

# Read the number of test cases
num_cases = int(input())

# Loop through each test case
for _ in range(num_cases):
    num = input()  # Read a phone number from the user
    res = pattern.findall(num)  # Use the regular expression to find all matches in the phone number
    
    # Check if there is a match
    if res:
        # Unpack the match groups
        country_code, local_area_code, number = res[0]
        # Print the formatted result
        print(f'CountryCode={country_code},LocalAreaCode={local_area_code},Number={number}')
