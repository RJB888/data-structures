"""Create hashing functions for hash table."""


class HashTable(object):
    """Create table class."""

    def __init__(self, size=137, method='additive'):
        """Initialize the hash table."""
        self.table = [[]] * size
        self.method = method

    def additive(self, word):
        """Simple additive hash."""
        total = 0
        for char in word:
            total += ord(char)
        return int(total % len(self.table))

    def horner(self, word):
        """Use horner better hash func."""
        MODIFIER = 37
        total = 0
        for char in word:
            total += MODIFIER * total + ord(char)
        return int(total % len(self.table))

    def get(self, key):
        """Return the value associated with the key."""
        try:
            if not isinstance(key, str):
                raise ValueError("Only strings allowed.")
            idx = self._hash(key)
            output = [tup for tup in self.table[idx] if tup[0] == key]
            return output[0][1]
        except(IndexError):
            return

    def set(self, key, val):
        """Store the given val using given key."""
        if not isinstance(key, str) or not isinstance(val, str):
            raise ValueError("Only strings allowed.")
        idx = self._hash(key)
        if self.table[idx]:
            self.table[idx].append((key, val))
        else:
            self.table[idx] = [(key, val)]

    def _hash(self, key):
        """Hash the provided key by hash type."""
        if self.method == "additive":
            idx = self.additive(key)
        else:
            idx = self.horner(key)
        return idx
