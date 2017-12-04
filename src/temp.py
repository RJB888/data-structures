
    #traversals follow:
    def in_order(self):
        """Generate numbers in order from tree."""
        stack = []
        cur = self.root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.l_child
            else:
                cur = stack.pop()
                yield cur.val
                cur = cur.r_child


    def in_order(self):
        """Return in-order traversal generator."""
        stack = []
        current = self._root
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                yield current.val
                current = current.right

    def pre_order(self):
        """Return pre-order traversal generator."""
        stack = [self._root]
        current = None
        while current or stack:
            if not current:
                current = stack.pop()
            else:
                yield current.val
                stack.extend([current.right, current.left])
                current = stack.pop()

    def post_order(self):
        """Return post-order traversal generator."""
        stack = []
        current = self._root
        while current or stack:
            if current:
                if current.right:
                    stack.append(current.right)
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                if stack and current.right == stack[-1]:
                    stack.pop()
                    stack.append(current)
                    current = current.right
                else:
                    yield current.val
                    current = None

    def breadth_first(self):
        """Return breadth-first traversal generator."""
        que = []
        current = self._root
        while current or que:
            if current:
                yield current.val
                que.extend([current.left, current.right])
                current = que.pop(0)
            else:
                current = que.pop(0)