"""Implement a Trie tree to store words."""


class Node(object):
    """Create a node."""

    def __init__(self, val):
        """Initialize node object."""
        if isinstance(val, str):
            self.val = val
            self.children = {}
        else:
            raise ValueError("Strings only.")


class Trie(object):
    """Create a Trie tree object."""

    def __init__(self):
        """Initialize the tree."""
        self.head = Node('*')
        self.count = 0

    def insert(self, val):
        """Insert a value into the Trie."""
        pass

    def contains(self, val):
        """Return true if val in tree, else false."""
        pass

    def size(self):
        """Return size of tree."""
        return self.count

    def remove(self, val):
        """Remove given value from tree."""
        if len(self.head.children) < 1:
            raise IndexError("list is empty")
        raise ValueError
