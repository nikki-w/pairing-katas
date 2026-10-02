# Test file for sum_digits
from sum_digits import sum_digits


def test_sum_digits_returns_integer_value():
    """Tests if sum_digits function returns an integer value."""
    assert type(sum_digits(1)) == int
    assert type(sum_digits(145)) == int

def test_sum_digits_returns_sum_of_all_numbers_for_int_value():
    """Tests if the sum_digits function returns a sum of all input 
    numbers for integer input."""
    assert sum_digits(1234) == 10
    assert sum_digits(176) == 14

def test_sum_digits_returns_sum_of_all_numbers_for_float_value():
    """Tests if the sum_digits function returns a sum of all input 
    numbers for float input."""
    assert sum_digits(1.234) == 10
    assert sum_digits(17.6) == 14

def test_sum_digits_returns_sum_of_all_numbers_for_negative_input():
    """Tests if the sum_digits function returns a sum of all input 
    numbers for float input."""
    assert sum_digits(-1234) == 10
    assert sum_digits(-17.6) == 14