"""A testing suite for trie data structure."""
from trie import TrieTree
import pytest


@pytest.fixture
def empty_trie():
    """And empty TrieTree."""
    return TrieTree()


@pytest.fixture
def three_word_trie_no_overlap():
    """A trie with three words that do not overlap."""
    new_trie = TrieTree()
    new_trie.insert('cat')
    new_trie.insert('bear')
    new_trie.insert('mouse')
    return new_trie


@pytest.fixture
def three_word_trie_with_overlap():
    """A trie with three words that will overlap."""
    new_trie = TrieTree()
    new_trie.insert('cake')
    new_trie.insert('car')
    new_trie.insert('carpet')
    return new_trie


@pytest.fixture
def six_word_trie_with_some_overlap():
    """A trie with six words that will have some overlap."""
    new_trie = TrieTree()
    new_trie.insert('cake')
    new_trie.insert('car')
    new_trie.insert('carpet')
    new_trie.insert('rats')
    new_trie.insert('ratchet')
    new_trie.insert('knife')
    return new_trie


@pytest.fixture
def twelve_word_trie_with_some_overlap():
    """A trie with twelve words that will have some overlap."""
    new_trie = TrieTree()
    new_trie.insert('garden')
    new_trie.insert('gardener')
    new_trie.insert('bottle')
    new_trie.insert('computer')
    new_trie.insert('battle')
    new_trie.insert('motorcycle')
    new_trie.insert('motley')
    new_trie.insert('dagger')
    new_trie.insert('hatchet')
    new_trie.insert('hatch')
    new_trie.insert('alphabet')
    new_trie.insert('Seattle')
    return new_trie


def test_insert_repeat_val(three_word_trie_with_overlap):
    """Test an appropriate error is raised when duplicate value inserted."""
    with pytest.raises(ValueError):
        three_word_trie_with_overlap.insert('cake')


def test_empty_trie_insert(empty_trie):
    """Test insert on an empty trie."""
    empty_trie.insert('pie')
    empty_trie.insert('cake')
    assert empty_trie.size() == 2
    assert empty_trie.contains('cake') is True
    assert empty_trie.contains('pie') is True


def test_insert_with_overlap(twelve_word_trie_with_some_overlap):
    """Test insert correctly handles overlap."""
    twwo = twelve_word_trie_with_some_overlap
    twwo.insert('competition')
    twwo.insert('hacker')
    assert twwo.size() == 14
    assert twwo.contains('competition') is True
    assert twwo.contains('hacker') is True
    assert twwo.contains('hatchet') is True
    assert twwo.contains('computer') is True


def test_contains_returns_true_when_true(twelve_word_trie_with_some_overlap):
    """Test the contain method works correctly when word is in TrieTree."""
    twwo = twelve_word_trie_with_some_overlap
    assert twwo.contains('hatch') is True
    assert twwo.contains('dagger') is True
    assert twwo.contains('Seattle') is True


def test_contains_returns_false_when_false(six_word_trie_with_some_overlap):
    """Test the contain method works correctly when word isn't in TrieTree."""
    six = six_word_trie_with_some_overlap
    assert six.contains('batch') is False
    assert six.contains('baker') is False
    assert six.contains('portland') is False


def test_size_of_empty_trie(empty_trie):
    """Test empty trie returns size of zero."""
    assert empty_trie.size() == 0


def test_size_on_twelve_trie(twelve_word_trie_with_some_overlap):
    """Test the size function on twelve word trie returns twelve."""
    assert twelve_word_trie_with_some_overlap.size() == 12


def test_remove_correctly_removes(three_word_trie_no_overlap):
    """Test that a word is correctly removed from trie."""
    three_word_trie_no_overlap.remove('cat')
    assert three_word_trie_no_overlap.size() == 2
    assert three_word_trie_no_overlap.contains('cat') is False


def test_remove_multiple_words(twelve_word_trie_with_some_overlap):
    """Test the removal of three words from twelve word TrieTree."""
    twwo = twelve_word_trie_with_some_overlap
    twwo.remove('Seattle')
    assert twwo.size() == 11
    assert twwo.contains('Seattle') is False
    twwo.remove('dagger')
    assert twwo.size() == 10
    assert twwo.contains('dagger') is False
    twwo.remove('garden')
    assert twwo.size() == 9
    assert twwo.contains('garden') is False


def test_contains_case_sensative(twelve_word_trie_with_some_overlap):
    """Test that the tree is case sensative."""
    twwo = twelve_word_trie_with_some_overlap
    assert twwo.contains('seattle') is False
    assert twwo.contains('Seattle') is True
    twwo.insert('seattle')
    assert twwo.contains('seattle') is True
    assert twwo.contains('Seattle') is True


def test_remove_string_not_in_tree(six_word_trie_with_some_overlap):
    """Test removing a string not in the tree raises error."""
    six = six_word_trie_with_some_overlap
    with pytest.raises(ValueError):
        six.remove('bananza')


def test_non_string_insert(empty_trie):
    """Test that an error is raised if you try to insert a non string."""
    with pytest.raises(TypeError):
        empty_trie.insert(1)


def test_non_string_remove(empty_trie):
    """Test that an error is raised if you try to remove a non string."""
    with pytest.raises(TypeError):
        empty_trie.remove((3, 'word', 'pickles'))


def test_non_string_contains(empty_trie):
    """Test that an error is raised if you try to check for a non string."""
    with pytest.raises(TypeError):
        empty_trie.contains([{}, {}, {}])


def test_depth_traversal_from_root(twelve_word_trie_with_some_overlap):
    """Test full word depth traversal of twelve word tree."""
    twwo = twelve_word_trie_with_some_overlap.depth_traversal('b')
    assert next(twwo) == 'b'
    assert next(twwo) == 'o'
    assert next(twwo) == 't'
    assert next(twwo) == 't'
    assert next(twwo) == 'l'
    assert next(twwo) == 'e'
    assert next(twwo) == 'a'
    assert next(twwo) == 't'
    assert next(twwo) == 't'
    assert next(twwo) == 'l'
    assert next(twwo) == 'e'


def test_depth_traversal_from_deeper_node(six_word_trie_with_some_overlap):
    """Test a traversal with a larger prefix."""
    six = six_word_trie_with_some_overlap
    six.insert('carpenter')
    six.insert('carp')
    six = six.depth_traversal('carp')
    assert next(six) == 'carp'
    assert next(six) == 'e'
    assert next(six) == 't'
    assert next(six) == 'n'
    assert next(six) == 't'
    assert next(six) == 'e'
    assert next(six) == 'r'


def test_depth_traversal_non_prefix(six_word_trie_with_some_overlap):
    """Test error is raised if start is not a prefix in the tree."""
    six = six_word_trie_with_some_overlap.depth_traversal('a')
    with pytest.raises(ValueError):
        next(six)


def test_depth_traversal_non_end_of_prefix(twelve_word_trie_with_some_overlap):
    """Test error is raised when later parts of start are not in tree."""
    twwo = twelve_word_trie_with_some_overlap.depth_traversal('gr')
    with pytest.raises(ValueError):
        next(twwo)


def test_depth_traversal_bad_type(three_word_trie_no_overlap):
    """Test error is raised if start is not a string."""
    three = three_word_trie_no_overlap.depth_traversal(1)
    with pytest.raises(TypeError):
        next(three)
