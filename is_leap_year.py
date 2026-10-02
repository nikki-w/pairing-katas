# File containing a function called is_leap_year that 
# takes a year as a number and returns True if it's a 
# leap year, and False otherwise.

def is_leap_year(year):
    """Function called is_leap_year that 
    takes a year as a number and returns True if it's a 
    leap year, and False otherwise."""
    if year % 4 == 0 and not year / 100:
        return True
    if year % 4 == 0 and year / 400:
        return True
    return False