# Function that takes a list of numbers and returns True 
# if all the numbers are in ascending order, and False if they are not.

def are_ordered(list_of_numbers):
    """Function that takes a list of numbers and returns True 
    if all the numbers are in ascending order, and False if they 
    are not."""
    if sorted(list_of_numbers):
        return True
    if list_of_numbers == []:
        return False