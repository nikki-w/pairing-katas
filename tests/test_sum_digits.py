# Test file for sum_digits
from sum_digits import sum_digits


def test_sum_digits_returns_integer_value():
    """Tests if sum_digits function returns an integer value"""
    assert type(sum_digits(1)) == int
    assert type(sum_digits(1.45)) == int