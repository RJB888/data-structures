"""Test Insertion Sort function."""


import pytest
import random


def test_empty_list_raises_error():
    """Test that an empty list raises an index error."""
    from insertion import insertion_sort
    with pytest.raises(IndexError):
        insertion_sort([])


def test_small_list_is_sorted():
    """Test that an empty list raises an index error."""
    from insertion import insertion_sort
    x = random.sample(range(30), 4)
    assert insertion_sort(x) == sorted(x)


def test_large_list_is_sorted():
    """Test that an empty list raises an index error."""
    from insertion import insertion_sort
    x = random.sample(range(200), 50)
    assert insertion_sort(x) == sorted(x)


def test_insertion_sort_sorts_letters():
    """Test that function will sort list of letters."""
    from insertion import insertion_sort
    x = random.sample(range(65, 123), 5)
    y = [chr(n) for n in x]
    assert insertion_sort(y) == sorted(y)
