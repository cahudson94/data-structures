"""Test suite for hash tables."""
from hash_table import HashTable
from os import path
import pytest
from faker import Faker


dictionary = path.realpath(__file__).replace('test_hash.py',
                                             'words')

with open(dictionary, 'r') as dictionary:
    dictionary_words = dictionary.read()


@pytest.fixture
def dictionary_filled_hash_table_one_bucket(dictionary_words):
    """Test for hash table with one bucket, dictionary."""
    ht = HashTable(1)
    for word in dictionary_words:
        ht.set(word[:-1], word[:-1])
    return ht


@pytest.fixture
def dictionary_filled_hash_table_ten_buckets(dictionary_words):
    """Test for hash table with ten buckets, dictionary."""
    ht = HashTable(10)
    for word in dictionary_words:
        ht.set(word[:-1], word[:-1])
    return ht


@pytest.fixture
def dictionary_filled_hash_table_100_buckets(dictionary_words):
    """Test for hash table with 100 buckets, dictionary."""
    ht = HashTable(100)
    for word in dictionary_words:
        ht.set(word[:-1], word[:-1])
    return ht


@pytest.fixture
def dictionary_filled_hash_table_1000_buckets(dictionary_words):
    """Test for hash table with 1000 buckets, dictionary."""
    ht = HashTable(1000)
    for word in dictionary_words:
        ht.set(word[:-1], word[:-1])
    return ht


@pytest.fixture
def hash_table_with_string_numbers():
    """Test for hash table with string numbers."""
    ht = HashTable(20)
    for i in range(100):
        ht.set(str(i), str(i * 2))
    return ht


@pytest.fixture
def hash_table_with_letters_and_numbers():
    """Test for hash table with both string letters and numbers."""
    ht = HashTable(30)
    stuff = []
    for i in range(50):
        stuff.append(str(i))
    # not done yet
    return


def test_get_five_times_dict_one_bucket(dictionary_filled_hash_table_one_bucket):
    """Test five items are in correct location."""
    ht = dictionary_filled_hash_table_one_bucket
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
    assert ('bolts', 'nuts') in ht._buckets[bolt_bucket].search(bolts_hash)._list
    assert ('sacks', 'spaghetti') in ht._buckets[sack_bucket].search(sacks_hash)._list
