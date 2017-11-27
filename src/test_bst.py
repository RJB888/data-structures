"""Test functionality of BST."""

import pytest


def test_bst():
    """Test that BST instantiates."""
    from bst import BST
    tree = BST()
    assert tree
