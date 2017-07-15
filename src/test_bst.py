"""Testing suite for Binary Search Tree data structure."""
import pytest
from bst import BST
from bst import Node


@pytest.fixture
def empty_bst():
    """Create empty BST."""
    return BST()


@pytest.fixture
def one_node_bst():
    """One node BST."""
    one_node = BST()
    one_node.insert(5)
    return one_node


@pytest.fixture
def three_node_bst():
    """A BST initialied with three nodes."""
    three_node = BST()
    three_node.insert(5)
    three_node.insert(23)
    three_node.insert(11)
    return three_node


@pytest.fixture
def three_node_bst_with_list():
    """A BST initialied with three nodes from list."""
    three_node = BST([2, 1, 3])
    return three_node


@pytest.fixture
def five_node_bst_with_tuple():
    """A BST initialied with five nodes from tuple."""
    five_node = BST((6, 4, 8, 7, 6.5))
    return five_node


@pytest.fixture
def five_node_bst_by_insert():
    """A BST initialied with five nodes from insert."""
    five_node = BST()
    five_node.insert(6)
    five_node.insert(2)
    five_node.insert(11)
    five_node.insert(4.2)
    five_node.insert(1)
    return five_node


@pytest.fixture
def ten_node_bst_with_list():
    """A BST initialied with ten nodes from list."""
    ten_node = BST([10, 7, 12, 4, 9, 23, 2, 5, 17, 50])
    return ten_node


@pytest.fixture
def left_side_bst():
    """A BST with only left nodes."""
    left = BST([34, 22, 32, 20, 15, 21, 6])
    return left


@pytest.fixture
def right_side_bst():
    """A BST with only right nodes."""
    right = BST([2, 14, 22, 10, 8, 6, 31, 55, 66, 77])
    return right


@pytest.fixture
def wonky_bst():
    """A BST that goes all over."""
    wonky = BST([40, 22, 34, 30, 32, 55, 66, 77, 68, 1, 2, 3, 99, 4, 5, 6, 7])
    return wonky


def test_empty_bst_features(empty_bst):
    """Test base features of empty BST."""
    assert empty_bst._root is None
    assert empty_bst._length == 0
    assert empty_bst._depth == 0
    assert empty_bst._balance == 0


def test_empty_bst_size_returns_0(empty_bst):
    """Test size of empty BST."""
    assert empty_bst.size() == 0


def test_empty_bst_depth_returns_0(empty_bst):
    """Test depth of empty BST."""
    assert empty_bst.depth() == 0


def test_empty_bst_balance_returns_0(empty_bst):
    """Test balance of empty BST."""
    assert empty_bst.balance() == 0


def test_init_with_int():
    """Test initalization of BST with an integer."""
    one_int = BST(10284)
    assert one_int.size() == 1
    assert one_int._root.val == 10284


def test_search_with_bad_data_type(one_node_bst):
    """Test bad data on search raises error."""
    with pytest.raises(TypeError):
        one_node_bst.search('five')


def test_contains_with_bad_data_type(one_node_bst):
    """Test bad data on contains raises error."""
    with pytest.raises(TypeError):
        one_node_bst.contains('lskdfj')


def test_repeat_val_insert_attempt_fails(one_node_bst):
    """Test that insert an exisiting val returns None."""
    assert one_node_bst.insert(5) is None


def test_one_node_bst_val_is_root(one_node_bst):
    """Test that a BST with one node has root of one node."""
    assert one_node_bst._root.val == 5


def test_one_node_bst_correct_size(one_node_bst):
    """Test that a BST with one node returns correct size."""
    assert one_node_bst.size() == 1


def test_one_node_bst_correct_balance(one_node_bst):
    """Test that one node BST returns balance of 0."""
    assert one_node_bst.balance() == 0


def test_one_node_bst_correct_depth(one_node_bst):
    """Test one node BST returns depth of 1."""
    assert one_node_bst.depth() == 1


def test_one_node_bst_search_returns_node(one_node_bst):
    """Test that one node BST search of one node's val returns root."""
    assert one_node_bst.search(5) == one_node_bst._root


def test_one_node_bst_contains_returns_true(one_node_bst):
    """Test one node BST contains val of one node."""
    assert one_node_bst.contains(5) is True


def test_one_node_bst_contains_returns_false(one_node_bst):
    """Test one node BST does not contain other value."""
    assert one_node_bst.contains(3145) is False


def test_three_node_bst_correct_size(three_node_bst):
    """Test that a three node BST returns 3."""
    assert three_node_bst.size() == 3


def test_three_node_bst_correct_balance(three_node_bst_with_list):
    """Test three node BST returns correct balance."""
    assert three_node_bst_with_list.balance() == -1


def test_three_node_bst_correct_depth(three_node_bst):
    """Test three node BST returns correct depth."""
    assert three_node_bst.depth() == 3


def test_three_node_bst_search_returns_node(three_node_bst_with_list):
    """Test three node BST search returns node searched for."""
    assert isinstance(three_node_bst_with_list.search(2), Node)
    assert three_node_bst_with_list.search(2).val == 2


def test_three_node_bst_contains_returns_true(three_node_bst):
    """Test three node BST contains two nodes that are in the BST."""
    assert three_node_bst.contains(5) is True
    assert three_node_bst.contains(23) is True


def test_three_node_bst_contains_returns_false(three_node_bst):
    """Test BST does returns false on bad node val."""
    assert three_node_bst.contains(3145) is False


def test_five_node_bst_correct_size(five_node_bst_with_tuple):
    """Test the size of a BST with 5 nodes."""
    assert five_node_bst_with_tuple.size() == 5


def test_five_node_bst_correct_balance(five_node_bst_by_insert):
    """Test the balance of a 5 node BST."""
    assert five_node_bst_by_insert.balance() == -2


def test_five_node_bst_correct_depth(five_node_bst_with_tuple):
    """Test the depth of a five node BST."""
    assert five_node_bst_with_tuple.depth() == 4


def test_five_node_bst_search_returns_node(five_node_bst_by_insert):
    """Test five node BST search returns node searched for."""
    assert isinstance(five_node_bst_by_insert.search(4.2), Node)
    assert five_node_bst_by_insert.search(4.2).val == 4.2


def test_five_node_bst_contains_returns_true(five_node_bst_with_tuple):
    """Test BST contains function of a five node BST."""
    assert five_node_bst_with_tuple.contains(6.5) is True
    assert five_node_bst_with_tuple.contains(4) is True


def test_five_node_bst_contains_returns_false(five_node_bst_by_insert):
    """Test bad contain function with val not in BST."""
    assert five_node_bst_by_insert.contains(3145) is False


def test_ten_node_bst_correct_size(ten_node_bst_with_list):
    """Test the size of a 10 node BST."""
    assert ten_node_bst_with_list.size() == 10


def test_ten_node_bst_correct_balance(ten_node_bst_with_list):
    """Test the balance of ten node BST."""
    assert ten_node_bst_with_list.balance() == -3


def test_ten_node_bst_correct_depth(ten_node_bst_with_list):
    """Test the depth of a 10 node BST."""
    assert ten_node_bst_with_list.depth() == 4


def test_init_bst_raises_type_error_with_dict():
    """Test init with dict raises TypeError."""
    with pytest.raises(TypeError):
        BST({4: 6, 5: 7, 3: 3})


def test_init_bst_raises_type_error_with_boolean():
    """Test init BST with boolean raises TypeError."""
    with pytest.raises(TypeError):
        BST(True)


def test_init_bst_raises_type_error_with_str():
    """Test init with str raises TypeError."""
    with pytest.raises(TypeError):
        BST('hiii')


def test_init_bst_raises_type_error_with_bad_data_in_list():
    """Test init with bad data in list raises TypeError."""
    with pytest.raises(TypeError):
        BST([4, '23', 'balls'])


def test_insert_with_bad_val_raises_type_error(one_node_bst):
    """Test insert with bad val raises TypeError."""
    with pytest.raises(TypeError):
        one_node_bst.insert('howdy')


def test_insert_with_list_raises_type_error(one_node_bst):
    """Test insert with list raises TypeError."""
    with pytest.raises(TypeError):
        one_node_bst.insert([23, 44])


def test_blance_and_depth_of_wonky_bst(wonky_bst):
    """Test the balance of the wonky bst."""
    assert wonky_bst.balance() == -8
    assert wonky_bst.depth() == 9


def test_blance_and_depth_of_right_bst(right_side_bst):
    """Test the balance of the right bst."""
    assert right_side_bst.balance() == 6
    assert right_side_bst.depth() == 7


def test_blance_and_depth_of_left_bst(left_side_bst):
    """Test the balance of the left bst."""
    assert left_side_bst.balance() == -4
    assert left_side_bst.depth() == 5
