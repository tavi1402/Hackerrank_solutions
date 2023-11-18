if __name__ == '__main__':
    # Get user input for a string 's'.
    s = input()
    
    # Check if there is at least one alphanumeric character in the string 's'.
    print(any(map(str.isalnum, s)))
    
    # Check if there is at least one alphabetical character in the string 's'.
    print(any(map(str.isalpha, s)))
    
    # Check if there is at least one digit in the string 's'.
    print(any(map(str.isdigit, s)))
    
    # Check if there is at least one lowercase character in the string 's'.
    print(any(map(str.islower, s)))
    
    # Check if there is at least one uppercase character in the string 's'.
    print(any(map(str.isupper, s)))
