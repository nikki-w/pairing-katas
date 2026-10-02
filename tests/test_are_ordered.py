# Tests for are_ordered.py
from are_ordered import are_ordered

def test_are_ordered_returns_False_for_empty_list():
    """Tests are_ordered..."""
    assert are_ordered([]) == False