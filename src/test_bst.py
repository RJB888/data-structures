"""Test functionality of BST."""

import pytest


def test_bst():
    """Test that BST instantiates."""
    from bst import BST
    tree = BST()
    assert tree


def test_bst_insert():
    """Test insert adds a node."""
    from bst import BST
    tree = BST()
    tree.insert(2)
    assert tree.root.val == 2

def test_multiple_insert():
    """Test multiple insertions."""
    from bst import BST
    tree = BST()
    tree.insert(3)
    tree.insert(5)
    tree.insert(6)
    assert tree.size() == 3

def test_bst_insert_list():
    """Test inserting iterable works."""
    from bst import BST
    my_list = [3, 5, 6, 10]
    tree = BST(my_list)
    assert tree.size() == 4
    assert tree.root.val == 3

def test_bst_insert_non_sequential():
    """Test insert functionality on non-sequential input."""
    from bst import BST
    my_list = [10, 5, 3, 8, 12]
    tree = BST(my_list)
    assert tree.size() == 5
    assert tree.root.val == 10

def test_bst_insert_tuple():
    """Test inserting iterable works."""
    from bst import BST
    my_list = (3, 5, 6, 10)
    tree = BST(my_list)
    assert tree.size() == 4
    assert tree.root.val == 3

def test_bst_size_works():
    """Test size function."""
    from bst import BST
    tree = BST()
    tree.insert(2)
    assert tree.size() == 1

def test_bst_balance():
    """Test balance gives right value."""
    from bst import BST
    tree = BST([10, 5, 3, 8, 12, 15, 2, 1])
    assert tree.balance() == 3

def test_bst_size_on_large_tree():
    """Test bst size with larger tree."""
    from bst import BST
    tree = BST([10, 5, 3, 8, 12, 15, 2, 1])
    assert tree.size() == 8

def test_bst_contains_value():
    """Test that contains works."""
    from bst import BST
    tree = BST([10, 5, 3, 8, 12, 15, 2, 1])
    assert tree.contains(12)
    assert tree.contains(10)
    assert tree.contains(2)

def test_bst_search_gives_proper_node():
    """Test that search gives node with proper value."""
    from bst import BST
    tree = BST([10, 5, 3, 8, 12, 15, 2, 1])
    assert tree.search(3)
    assert tree.search(3).val == 3

def test_insert_non_integer_raises_error():
    """Test that inserting an integer raises value error."""
    from bst import BST
    tree = BST()
    with pytest.raises(ValueError):
        tree.insert('q')

def test_duplicate_value_insertion_ignored():
    """Test that attempt to insert duplicate value is ignored."""
    from bst import BST
    tree = BST()
    tree.insert(1)
    tree.insert(1)
    assert tree.size() == 1