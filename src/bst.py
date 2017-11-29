"""Create a binary search tree with the following functionality."""


class Node(object):
    """Create a node to be used in the BST."""

    def __init__(self, val):
        """Initialize Node."""
        self.l_child = None
        self.r_child = None
        self.parent = None
        self.val = val


class BST(object):
    """Create the BST functionality."""

    def __init__(self, iterable=None):
        """Initialize the tree."""
        self.node_count = 0
        self.r_depth = 0
        self.l_depth = 0
        self._balance = 0
        self.root = None
        if isinstance(iterable, (list, tuple)):
            for item in iterable:
                self.insert(item)

    def insert(self, val):
        """Insert val into BST, if val is already there, ignore insertion."""
        if not isinstance(val, (int, float)):
            raise ValueError("Only numbers are allowed.")
        if self.node_count == 0:
            self.root = Node(val)
            self.node_count += 1
            return
        elif self.contains(val):
            return
        cur = self.root
        if val < self.root.val:
            self._balance += 1
        else:
            self._balance -= 1
        while cur:
            if val < cur.val:
                self.l_depth += 1
                if cur.l_child:
                    cur = cur.l_child
                else:
                    cur.l_child = Node(val)
                    cur.l_child.parent = cur
                    self.node_count += 1
                    break
            else:
                self.r_depth += 1
                if cur.r_child:
                    cur = cur.r_child
                else:
                    cur.r_child = Node(val)
                    cur.r_child.parent = cur
                    self.node_count += 1
                    break

    def search(self, val):
        """Return the NODE containing that val. Else: None."""
        cur = self.root
        while cur:
            if val == cur.val:
                return cur
            elif val < cur.val:
                cur = cur.l_child
            elif val > cur.val:
                cur = cur.r_child

    def size(self):
        """Return the int size of the BST. (# of nodes in tree, 0 if None."""
        return self.node_count

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
        return self._balance

    def _delete_with_one_child(self, cur):
        """Delete node with only one child."""
        if cur.l_child:
            if cur.parent.l_child == cur:
                cur.parent.l_child = cur.l_child
            else:
                cur.parent.r_child = cur.l_child
        else:  # cur has r_child
            if cur.parent.l_child == cur:
                cur.parent.l_child = cur.r_child
            else:
                cur.parent.r_child = cur.r_child

    def _delete_with_two_children(self, cur):
        """Remove a node with two children."""
        old_root = cur
        new_root = cur.l_child
        while new_root:
            if new_root.r_child:
                new_root = new_root.r_child
            else:
                break
        new_root.r_child = old_root.r_child
        new_root.parent = old_root.parent
        if new_root.l_child:
            new_root.parent.r_child = new_root.l_child
        elif new_root.parent != old_root:
            new_root.l_child = old_root.l_child
        if cur == self.root:
            self.root = new_root

    def delete(self, val):
        """Remove indicated node from tree."""
        cur = self.search(val)
        if cur.l_child and cur.r_child:
            self._delete_with_two_children(cur)
        elif cur.l_child or cur.r_child:
            self._delete_with_one_child(cur)
        else:
            rem = self.search(val)
            if rem == self.root:
                self.root = None
            elif rem.parent.l_child == rem:
                rem.parent.l_child = None
            else:
                rem.parent.r_child = None
        self.node_count -= 1
    if __name__ == '__main__':  # pragma: no cover
        import timeit as ti
        import BST
        first_tree = BST([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        second_tree = BST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        third_tree = BST([5, 6, 4, 7, 3, 8, 2, 9, 1, 10])

        t1 = ti.timeit("first_tree.search(5)",
                       setup="from __main__ import first_tree")
        t2 = ti.timeit("second_tree.search(5)",
                       setup="from __main__ import second_tree")
        t3 = ti.timeit("third_tree.search(8)",
                       setup="from __main__ import third_tree")

        print('Negatively skewed tree search time: ', t1)
        print('Positively skewed tree search time: ', t2)
        print('Balanced tree search time: ', t3)
