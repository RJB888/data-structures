"""Test the merge sort function."""

import random


def test_empty_list_raises_error():
    """Test that an empty list raises an index error."""
    from merge import merge
    assert merge([]) == []


def test_small_list_is_sorted():
    """Test that an empty list raises an index error."""
    from merge import merge
    x = random.sample(range(30), 4)
    assert merge(x) == sorted(x)


def test_large_list_is_sorted():
    """Test that an empty list raises an index error."""
    from merge import merge
    x = random.sample(range(200), 50)
    assert merge(x) == sorted(x)
