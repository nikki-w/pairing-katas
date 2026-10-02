# File containing a function called is_leap_year that 
# takes a year as a number and returns True if it's a 
# leap year, and False otherwise.

def is_leap_year(year):
    """Function called is_leap_year that 
    takes a year as a number and returns True if it's a 
    leap year, and False otherwise."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False 
        else:
            return True
    else:
        return False
