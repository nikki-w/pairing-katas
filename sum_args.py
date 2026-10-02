# File containing a function called sum_args that accepts any 
# number of arguments and adds them together.

def sum_args(*args):
    """Function that accepts any number of arguments 
    and adds them together."""
    if not args:
        return 0