# Test file for max_and_min.py
from max_and_min import nc_max, nc_min


# Tests for nc_max

def test_nc_max_returns_0_for_empty_list():
    """Tests if nc_max returns 0 when the input list is empty"""
    assert nc_max([]) == 0