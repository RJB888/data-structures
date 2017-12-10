"""Run tests for bubble sort function."""

import pytest
import random


def test_empty_list_raises_error():
    """Test that an empty list raises an index error."""
    from bubble_sort import bubble_sort
    with pytest.raises(IndexError):
        bubble_sort([])


def test_small_list_is_sorted():
    """Test that an empty list raises an index error."""
    from bubble_sort import bubble_sort
    x = random.sample(range(30), 4)
    assert bubble_sort(x) == sorted(x)


def test_large_list_is_sorted():
    """Test that an empty list raises an index error."""
    from bubble_sort import bubble_sort
    x = random.sample(range(200), 50)
    assert bubble_sort(x) == sorted(x)


def test_bubble_sort_sorts_letters():
    """Test that function will sort list of letters."""
    from bubble_sort import bubble_sort
    x = random.sample(range(65, 123), 5)
    y = [chr(n) for n in x]
    assert bubble_sort(y) == sorted(y)
