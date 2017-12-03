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
    assert tree.balance(tree.root) == 2


def test_bst_balance_non_root():
    """Test balance gives right value."""
    from bst import BST
    tree = BST([10, 5, 3, 8, 12, 15, 2, 1])
    assert tree.balance(tree.search(5)) == 2


def test_bst_balance_gives_zero_balance():
    """Test balance gives right value."""
    from bst import BST
    tree = BST([10, 5, 3, 8, 12, 15, 11])
    assert tree.balance(tree.search(12)) == 0


def test_bst_size_on_large_tree():
    """Test bst size with larger tree."""
    from bst import BST
    tree = BST([10, 5, 3, 8, 12, 15, 13, 11])

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

# depth tests start


def test_bst_depth_gives_proper_value():
    """Test that search gives node with proper value."""
    from bst import BST
    tree = BST([10, 5, 3, 8, 12, 15, 2, 1, 0])
    assert tree.depth(tree.root) == 5


def test_bst_depth_tree_with_no_nodes():
    """Test that search gives node with proper value."""
    from bst import BST
    tree = BST()
    assert tree.depth(tree.root) == 0


def test_bst_depth_tree_with_one_nodes():
    """Test that search gives node with proper value."""
    from bst import BST
    tree = BST([1])
    assert tree.depth(tree.root) == 0
# NOTE: Balance tests test the depth, becuase balance calls depth.

# traversal tests


def test_breadth_first_traversal_no_values():
    """."""
    from bst import BST
    from types import GeneratorType
    tree = BST()
    assert isinstance(tree.breadth_first_traverse(), GeneratorType)


def test_depth_first_traversal_one_value():
    """."""
    from bst import BST
    tree = BST([1])
    gen = tree.breadth_first_traverse()
    my_list = []
    my_list.append(next(gen))
    assert my_list[0] == 1


def test_breadth_first_traversal_multiple_values():
    """."""
    from bst import BST
    tree = BST([10, 5, 3, 8, 12, 15, 2, 1, 0])
    gen = tree.breadth_first_traverse()
    my_list = []
    for item in gen:
        my_list.append(item)
    assert my_list == [10, 5, 12, 3, 8, 15, 2, 1, 0]


def test_in_order_traverse_no_value():
    """."""
    from bst import BST
    from types import GeneratorType
    tree = BST([])
    gen = tree.in_order_traverse()
    assert isinstance(gen, GeneratorType)


def test_in_order_traverse_one_value():
    """."""
    from bst import BST
    tree = BST([1])
    gen = tree.in_order_traverse()
    assert next(gen) == 1


def test_in_order_traversal_multiple_values():
    """."""
    from bst import BST
    tree = BST([10, 5, 3, 8, 12, 15, 2, 1, 0])
    my_list = []
    gen = tree.in_order_traverse()
    for item in gen:
        my_list.append(item)
    assert my_list == [0, 1, 2, 3, 5, 8, 10, 12, 15]


def test_preorder_traverse_no_value():
    """."""
    from bst import BST
    from types import GeneratorType
    tree = BST([])
    gen = tree.preorder_traverse()
    assert isinstance(gen, GeneratorType)


def test_preorder_traverse_one_value():
    """."""
    from bst import BST
    tree = BST([1])
    gen = tree.preorder_traverse()
    assert next(gen) == 1


def test_preorder_traversal_multiple_values():
    """."""
    from bst import BST
    tree = BST([10, 5, 3, 8, 12, 15, 2, 1, 0])
    my_list = []
    gen = tree.preorder_traverse()
    for item in gen:
        my_list.append(item)
    assert my_list == [10, 5, 3, 2, 1, 0, 8, 12, 15]


def test_postord_traverse_no_value():
    """."""
    from bst import BST
    from types import GeneratorType
    tree = BST([])
    gen = tree.postorder_traverse()
    assert isinstance(gen, GeneratorType)


def test_postord_traverse_one_value():
    """."""
    from bst import BST
    tree = BST([1])
    gen = tree.postorder_traverse()
    assert next(gen) == 1


def test_postord_traversal_multiple_values():
    """."""
    from bst import BST
    tree = BST([10, 5, 3, 8, 12, 15, 2, 1, 0])
    my_list = []
    gen = tree.postorder_traverse()
    for item in gen:
        my_list.append(item)
    assert my_list == [0, 1, 2, 3, 8, 5, 15, 12, 10]


# tree deletion tests start


def test_bst_delete_root_with_no_child():
    """."""
    from bst import BST
    tree = BST()
    tree.insert(1)
    tree.delete(1)
    assert tree.size() == 0


def test_bst_delete_root_with_one_child():
    """."""
    from bst import BST
    my_list = (3, 5, 6, 10)
    tree = BST(my_list)
    tree.delete(3)
    assert tree.size() == 3
    assert tree.contains(6)
    assert tree.contains(5)
    assert tree.contains(10)


def test_bst_delete_root_with_only_left_child():
    """."""
    from bst import BST
    my_list = (5, 3, 1, 0)
    tree = BST(my_list)
    tree.delete(5)
    assert tree.size() == 3
    assert tree.contains(0)
    assert tree.contains(3)
    assert tree.contains(1)
    assert tree.root.val == 3


def test_bst_delete_with_left_right_child():
    """."""
    from bst import BST
    my_list = (7, 5, 3, 4)
    tree = BST(my_list)
    tree.delete(3)
    assert tree.size() == 3
    assert tree.contains(5)
    assert tree.contains(7)
    assert tree.root.l_child.l_child.val == 4


def test_bst_delete_with_right_left_right_child():
    """."""
    from bst import BST
    my_list = (4, 7, 6, 5)
    tree = BST(my_list)
    tree.delete(7)
    assert tree.size() == 3
    assert tree.contains(5)
    assert not tree.contains(7)
    assert tree.contains(4)
    assert tree.root.r_child.l_child.val == 5


def test_bst_delete_root_with_two_children():
    """."""
    from bst import BST
    my_list = (3, 2, 5, 6, 10)
    tree = BST(my_list)
    tree.delete(3)
    assert tree.root.val == 2
    assert tree.size() == 4


def test_bst_delete_node_with_no_child():
    """."""
    from bst import BST
    my_list = (3, 5, 6, 10)
    tree = BST(my_list)
    tree.delete(10)
    assert tree.size() == 3
    assert not tree.contains(10)


def test_bst_delete_node_with_only_right_child():
    """."""
    from bst import BST
    my_list = (3, 5, 6, 10)
    tree = BST(my_list)
    tree.delete(5)
    assert not tree.contains(5)
    assert tree.size() == 3
    assert tree.root.r_child.val == 6


def test_bst_delete_node_with_only_left_child():
    """."""
    from bst import BST
    my_list = (5, 3, 1, 0)
    tree = BST(my_list)
    tree.delete(3)
    assert not tree.contains(3)
    assert tree.size() == 3
    assert tree.root.l_child.val == 1


def test_bst_delete_node_with_two_children():
    """."""
    from bst import BST
    my_list = (3, 2, 5, 6, 7, 10, 8)
    tree = BST(my_list)
    tree.delete(6)
    assert tree.root.r_child.r_child.val == 7


def test_bst_delete_node_with_two_children_left_side():
    """."""
    from bst import BST
    my_list = (4, 2, 3, 5, 6, 7, 10, 8)
    tree = BST(my_list)
    tree.delete(4)
    assert tree.root.val == 3
    assert tree.root.l_child.val == 2
