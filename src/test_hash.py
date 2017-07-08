"""Test suite for hash tables."""
from hash_table import HashTable, naive_hash
from os import path
import pytest
from faker import Faker


dictionary = path.realpath(__file__).replace('test_hash.py',
                                             'words')

with open(dictionary, 'r') as dictionary:
    dictionary_words = dictionary.read().split('\n')[:-1]


@pytest.fixture(scope='module')
def dict_hash_table_100_buckets():
    """Test for hash table with 100 buckets, dictionary."""
    ht = HashTable(100, naive_hash)
    for word in dictionary_words:
        ht.set(word, word)
    return ht


@pytest.fixture(scope='module')
def dict_hash_table_253_buckets():
    """Test for hash table with 253 buckets, dictionary."""
    ht = HashTable(253, naive_hash)
    for word in dictionary_words:
        ht.set(word, word)
    return ht


@pytest.fixture(scope='module')
def dict_hash_table_500_buckets():
    """Test for hash table with 500 buckets, dictionary."""
    ht = HashTable(500)
    for word in dictionary_words:
        ht.set(word, word)
    return ht


@pytest.fixture(scope='module')
def dict_hash_table_1000_buckets():
    """Test for hash table with 1000 buckets, dictionary."""
    ht = HashTable(1000)
    for word in dictionary_words:
        ht.set(word, word)
    return ht


@pytest.fixture(scope='module')
def hash_table_with_string_numbers():
    """Test for hash table with string numbers."""
    ht = HashTable(23)
    for i in range(100):
        ht.set(str(i), str(i * 2))
    return ht


@pytest.fixture(scope='module')
def hash_table_with_letters_and_numbers():
    """Test for hash table with both string letters and numbers."""
    ht = HashTable(3)
    stuff = []
    things = []
    for i in range(1500):
        stuff.append(str(i))
        things.append(Faker().text(8))
        ht.set(stuff[i], things[i])
    return ht


def test_get_five_times_dict_one_bucket(dict_hash_table_1000_buckets):
    """Test five items are in correct location."""
    ht = dict_hash_table_1000_buckets
    sizes = []
    for bst in ht._buckets:
        sizes.append(bst.size())
    print(sizes)
    assert ht.get('ball') == 'ball'
    assert ht.get('sack') == 'sack'
    assert ht.get('test') == 'test'
    assert ht.get('ice') == 'ice'
    assert ht.get('Stromboli') == 'Stromboli'


def test_set_two_times(hash_table_with_string_numbers):
    """Test that set goes to the expected node and bucket."""
    ht = hash_table_with_string_numbers
    ht.set('bolts', 'nuts')
    ht.set('sacks', 'spaghetti')
    bolts_hash = ht._hash('bolts')
    sacks_hash = ht._hash('sacks')
    bolt_bucket = bolts_hash % len(ht._buckets)
    sack_bucket = sacks_hash % len(ht._buckets)
    assert (('bolts', 'nuts') in
            ht._buckets[bolt_bucket].search(bolts_hash)._list)
    assert (('sacks', 'spaghetti') in
            ht._buckets[sack_bucket].search(sacks_hash)._list)


def test_key_not_in_hash_table(dict_hash_table_500_buckets):
    """Test that the given key is not in the table."""
    with pytest.raises(KeyError):
        dict_hash_table_500_buckets.get('gobledygook')


def test_naive_hash_get_five(dict_hash_table_253_buckets):
    """Test get on naive hash with minimal buckets."""
    ht = dict_hash_table_253_buckets
    assert ht.get('wombat') == 'wombat'


def test_naive_has_set_three(hash_table_with_letters_and_numbers):
    """Test the setting of two keys via naive hash."""
    ht = hash_table_with_letters_and_numbers
    ht.set('P07470', 'banana')
    ht.set('Onomatopoeia', 'Unctuous')
    po_hash = ht._hash('P07470')
    ono_hash = ht._hash('Onomatopoeia')
    po_bucket = po_hash % len(ht._buckets)
    ono_bucket = ono_hash % len(ht._buckets)
    assert (('P07470', 'banana') in
            ht._buckets[po_bucket].search(po_hash)._list)
    assert (('Onomatopoeia', 'Unctuous') in
            ht._buckets[ono_bucket].search(ono_hash)._list)


def test_key_replace_on_set_same_key(dict_hash_table_100_buckets):
    """Test that the key is replaced on set."""
    ht = dict_hash_table_100_buckets
    ball_hash = ht._hash('basketball')
    ball_bucket = ball_hash % len(ht._buckets)
    assert (('basketball', 'basketball') in
            ht._buckets[ball_bucket].search(ball_hash)._list)
    ht.set('basketball', 'balloon')
    assert (('basketball', 'balloon') in
            ht._buckets[ball_bucket].search(ball_hash)._list)
    assert (('basketball', 'basketball') not in
            ht._buckets[ball_bucket].search(ball_hash)._list)
