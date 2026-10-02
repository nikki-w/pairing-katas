# Tests for sum_args.py
from sum_args import sum_args

def test_sum_args_returns_0_when_no_arguments_given():
    """Tests if the sum_args function returns 0 when 
    no arguments are given."""
    assert sum_args() == 0