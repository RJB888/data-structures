"""Run tests for bubble sort function."""

import pytest
import random


random.sample(range(30), 4)


def test_empty_list_raises_error():
    """Test that an empty list raises an index error."""
    from bubble_sort import bubble_sort
    with pytest.raises(IndexError):
        bubble_sort()
