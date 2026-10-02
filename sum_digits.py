# File containing a function called sum_digits that takes a number (not necessarily an integer) 
# and returns the total of its digits.

def sum_digits(number):
    """Function that takes a number and returns the total of it's digits"""
    cleaned_number = str(number).replace('.', '')
    return sum(int(digit) for digit in cleaned_number)
            
if __name__ == "__main__":
    pass