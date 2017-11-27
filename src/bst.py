"""Create a binary search tree with the following functionality."""


class Node(object):
    """Create a node to be used in the BST."""

    def __init__(self, val):
        """Initialize Node."""
        self.l_child = None
        self.r_child = None
        self.val = 0


class BST(object):
    """Create the BST functionality."""

    def __init__(self, iterable=None):
        """Initialize the tree."""
        self.size = 0
        self.r_depth = 0
        self.l_depth = 0
        self.root = None
        if isinstance(iterable, (list, tuple)):
            for item in iterable:
                self.insert(item)

    def insert(self, val):
        """Insert val into BST, if val is already there, ignore insertion."""
        if not isinstance(val, [int, float]):
            raise ValueError("Only numbers are allowed.")
        if self.size == 0:
            self.root = Node(val)
            self.size += 1
            return
        elif self.contains(val):
            return
        cur = self.root
        while cur:
            if val < cur.val:
                self.l_depth += 1
                if cur.l_child:
                    cur = cur.l_child
                else:
                    cur.l_child = Node(val)
                    self.size += 1
            else:
                self.r_depth += 1
                if cur.r_child:
                    cur = cur.r_child
                else:
                    cur.r_child = Node(val)
                    self.size += 1

    def search(self, val):
        """Return the NODE containing that val. Else: None."""
        cur = self.root
        while cur:
            if val == cur.data:
                return cur
            elif val < cur.data:
                cur = cur.l_child
            elif val > cur.data:
                cur = cur.r_child

    def size(self):
        """Return the int size of the BST. (# of nodes in tree, 0 if None."""
        return self.size

    def depth(self):
        """Return int representation of the tree depth."""
        return self.l_depth if self.l_depth > self.r_depth else self.r_depth

    def contains(self, val):
        """Bool result for if val is in the tree."""
        if self.search(val):
            return True
        else:
            return False

    def balance(self):
        """Return an int (pos/neg) showing balance of the tree."""
        return self.l_depth - self.r_depth
