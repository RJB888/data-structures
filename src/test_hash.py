"""Test Hash Table Class."""


def test_hash_class():
    """Make sure class instantiates."""
    from hashing import HashTable
    tbl = HashTable()
    assert tbl.method == 'additive'
    assert len(tbl.table) == 137
