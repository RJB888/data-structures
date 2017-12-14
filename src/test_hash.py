"""Test Hash Table Class."""


def test_hash_class_default_build():
    """Make sure class instantiates."""
    from hashing import HashTable
    tbl = HashTable()
    assert tbl.method == 'additive'
    assert len(tbl.table) == 137


def test_additive_method():
    """Test that additive method hashes properly."""
    from hashing import HashTable
    tbl = HashTable()
    hashed = tbl.additive('aid')
    assert hashed == 28


def test_horner_method():
    """Test horner method hashes properly."""
    from hashing import HashTable
    tbl = HashTable()
    hashed = tbl.horner('aid')
    assert hashed == 34


def test_hash():
    """Test that _hash hashes the key according to hash type."""
    from hashing import HashTable
    tbl = HashTable()
    tbl2 = HashTable(137, 'horner')
    assert tbl._hash('boo') == 46
    assert tbl2._hash('boo') == 73


def test_get_method():
    """Test that get method retrieves value."""
    from hashing import HashTable
    tbl = HashTable()
    tbl.set('balloon', 'face')
    assert tbl.get('balloon') == 'face'


def test_get_on_empty_hashtable():
    """Test that getting a value on empty table returns none."""
    from hashing import HashTable
    tbl = HashTable()
    assert tbl.get("boom") is None


def test_get_value_not_in_hashtable():
    """Test that getting a value that isn't in the table returns none."""
    from hashing import HashTable
    tbl = HashTable()
    tbl.set('balloon', 'face')
    assert tbl.get("boom") is None


def test_set_method():
    """Test that set method sets key and value."""
    from hashing import HashTable
    tbl = HashTable()
    tbl.set('apple', 'apple')
    assert tbl.table
    assert tbl.table[tbl._hash('apple')][0][1] == 'apple'
