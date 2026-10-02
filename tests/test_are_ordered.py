# Tests for are_ordered.py
from are_ordered import are_ordered

def test_are_ordered_returns_false_for_empty_list():
    """Tests are_ordered returns False when input list is empty."""
    assert are_ordered([]) == False

def test_are_ordered_returns_true_for_numbers_in_ascending_order():
    """Tests if are_ordered returns True for inputs where numbers 
    are listed in ascending order."""
    assert are_ordered([1, 2, 3, 4]) == True
    assert are_ordered([12, 13, 14]) == True

def test_are_ordered_returns_false_for_numbers_not_in_ascending_order():
    """Tests if are_ordered returns True for inputs where numbers 
    are listed in ascending order."""
    assert are_ordered([3, 2, 8, 4]) == False
    assert are_ordered([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == False