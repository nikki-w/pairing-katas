# Test file for max_and_min.py
from max_and_min import nc_max, nc_min


# Tests for nc_max

def test_nc_max_returns_0_for_empty_list():
    """Tests if nc_max returns 0 when the input list is empty."""
    assert nc_max([]) == 0

def test_nc_max_returns_maximum_value_in_list():
    """Tests if nc_max returns minimum value in list."""
    assert nc_max([1, 7, 4, 5]) == 7

# Tests for nc_min

def test_nc_min_returns_0_for_empty_list():
    """Tests if nc_max returns 0 when the input list is empty."""
    assert nc_min([]) == 0

def test_nc_min_returns_minimum_value_in_list():
    """Tests if nc_max returns maximum value in list."""
    assert nc_min([4, 7, 1, 5]) == 1