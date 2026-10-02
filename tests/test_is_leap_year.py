# Tests for is_leap_year.py

from is_leap_year import is_leap_year

def test_is_leap_year_returns_bool():
    """Tests if is_leap_year returns bool."""
    assert is_leap_year(2020) == type(bool)
