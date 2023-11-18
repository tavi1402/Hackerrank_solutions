'''In this code, it creates a datetime.date object representing the input date and uses the weekday() method to 
obtain the day of the week as an integer (where Monday is 0 and Sunday is 6). It then accesses the day name from 
the calendar module using the obtained index and converts it to uppercase before printing it. The code determines 
and prints the day of the week for the given date.'''
# Import the datetime and calendar modules
import datetime
import calendar

# Read the input date as three integers (month, day, year)
m, d, y = map(int, input().split())

# Create a datetime.date object representing the input date
input_date = datetime.date(y, m, d)

# Use the weekday() method to get the day of the week (0=Monday, 1=Tuesday, ..., 6=Sunday)
# Then, access the corresponding day name from the calendar module and convert it to uppercase
day_name = calendar.day_name[input_date.weekday()].upper()

# Print the uppercase day name
print(day_name)
