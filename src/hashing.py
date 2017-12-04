"""Create hashing functions for hash table."""


class HashTable(object):
    """Create table class."""

    def __init__(self, size=137, method='additive'):
        """Initialize the hash table."""
        self.table = [None] * size
        self.method = method

    def additive(self, word):
        """Simple additive hash."""
        total = 0
        for char in word:
            total += ord(char)
            print(total)
        return int(total % len(self.table))

    def horner(self, word):
        """Use horner better hash func."""
        MODIFIER = 37
        total = 0
        for char in word:
            total += MODIFIER * total + ord(char)
            print(total)
        return int(total % len(self.table))

    def get(self, key):
        """Return the value associated with the key."""
        idx = self._hash(key)
        return self.table[idx]

    def set(self, key, val):
        """Store the given val using given key."""
        idx = self._hash(key)
        self.table[idx] = val

    def _hash(self, key):
        """Hash the provided key by hash type."""
        if self.method == "additive":
            idx = self.additive(key)
        else:
            idx = self.horner(key)
        return idx
