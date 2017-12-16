"""Test Insertion Sort function."""


import random


def test_empty_list_raises_error():
    """Test that an empty list raises an index error."""
    from quick import quick_sort
    assert quick_sort([]) == []


def test_small_list_is_sorted():
    """Test that small list sorts properly."""
    from quick import quick_sort
    x = random.sample(range(30), 4)
    assert quick_sort(x) == sorted(x)


def test_large_list_is_sorted():
    """Test that large list sorts properly."""
    from quick import quick_sort
    x = random.sample(range(200), 50)
    assert quick_sort(x) == sorted(x)


def test_quick_sort_sorts_letters():
    """Test that function will sort list of letters."""
    from quick import quick_sort
    x = random.sample(range(65, 123), 5)
    y = [chr(n) for n in x]
    assert quick_sort(y) == sorted(y)
