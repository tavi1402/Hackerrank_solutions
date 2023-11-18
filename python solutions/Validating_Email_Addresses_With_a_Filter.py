''' this code filters and validates a list of email addresses based on specific criteria and then 
prints the sorted list of valid email addresses.'''

# Define a function 'fun' to validate email addresses.
def fun(email):
    try:
        # Split the email address into username and URL.
        username, url = email.split('@')
        # Split the URL into website and extension.
        website, extension = url.split('.')
    except ValueError:
        # If any of the expected splits fails, return False (invalid email).
        return False

    # Check the following criteria for a valid email address:
    if username.replace('-', '').replace('_', '').isalnum() is False:
        return False
    elif website.isalnum() is False:
        return False
    elif len(extension) > 3:
        return False
    else:
        return True

# Define a function 'filter_mail' to filter a list of email addresses based on the 'fun' function.
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    # Read an integer 'n' from the user, indicating the number of email addresses.
    n = int(input())
    
    # Create an empty list 'emails' to store the email addresses.
    emails = []
    
    # Read 'n' email addresses from the user and append them to the 'emails' list.
    for _ in range(n):
        emails.append(input())

    # Use the 'filter_mail' function to filter the email addresses based on the 'fun' function.
    filtered_emails = filter_mail(emails)

    # Sort the valid email addresses in lexicographical order.
    filtered_emails.sort()

    # Print the sorted valid email addresses.
    print(filtered_emails)
