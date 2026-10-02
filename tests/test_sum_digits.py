# Test file for sum_digits
from sum_digits import sum_digits


def test_sum_digits_returns_integer_value():
    """Tests if sum_digits function returns an integer value."""
    assert type(sum_digits(1)) == int
    assert type(sum_digits(1.45)) == int

def test_sum_digits_returns_sum_of_all_numbers():
    """Tests if the sum_digits function returns a sum of all input numbers,
    regardless of their type"""
    assert sum_digits(1234) == 10
    assert sum_digits(1.234) == 10