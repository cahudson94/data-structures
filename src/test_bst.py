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
    """A BST initialized with three nodes."""
    three_node = BST()
    three_node.insert(5)
    three_node.insert(23)
    three_node.insert(11)
    return three_node


@pytest.fixture
def three_node_bst_with_list():
    """A BST initialized with three nodes from list."""
    three_node = BST([2, 1, 3])
    return three_node


@pytest.fixture
def five_node_bst_with_tuple():
    """A BST initialized with five nodes from tuple."""
    five_node = BST((6, 4, 8, 7, 6.5))
    return five_node


@pytest.fixture
def five_node_bst_by_insert():
    """A BST initialized with five nodes from insert."""
    five_node = BST()
    five_node.insert(6)
    five_node.insert(2)
    five_node.insert(11)
    five_node.insert(4.2)
    five_node.insert(1)
    return five_node


@pytest.fixture
def five_node_edge_case():
    """A BST initialized with five nodes for edge case."""
    five_node = BST()
    five_node.insert(6)
    five_node.insert(3)
    five_node.insert(2)
    five_node.insert(5)
    five_node.insert(4)
    return five_node


@pytest.fixture
def ten_node_bst_with_list():
    """A BST initialized with ten nodes from list."""
    ten_node = BST()
    ten_node.insert(10)
    ten_node.insert(7)
    ten_node.insert(12)
    ten_node.insert(4)
    ten_node.insert(9)
    ten_node.insert(23)
    ten_node.insert(2)
    ten_node.insert(5)
    ten_node.insert(17)
    ten_node.insert(50)
    return ten_node


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
    assert three_node_bst_with_list.balance() == 0


def test_three_node_bst_correct_depth(three_node_bst):
    """Test three node BST returns correct depth."""
    assert three_node_bst.depth() == 2


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
    assert five_node_bst_by_insert.balance() == -1


def test_five_node_bst_correct_depth(five_node_bst_with_tuple):
    """Test the depth of a five node BST."""
    assert five_node_bst_with_tuple.depth() == 3


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
    assert ten_node_bst_with_list.balance() == 0


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


def test_in_order_traversal_one_node(one_node_bst):
    """Test one node BST returns one val at a time.

    Uses 'in order' order.
    """
    one = one_node_bst.in_order()
    assert next(one) == 5


def test_in_order_traversal_five_node(five_node_bst_with_tuple):
    """Test five node BST returns one val at a time.

    Uses 'in order' order.
    """
    five = five_node_bst_with_tuple.in_order()
    assert next(five) == 4
    assert next(five) == 6
    assert next(five) == 6.5
    assert next(five) == 7
    assert next(five) == 8


def test_in_order_traversal_ten_node(ten_node_bst_with_list):
    """Test ten node BST returns one val at a time.

    Uses 'in order' order.
    """
    ten = ten_node_bst_with_list.in_order()
    assert next(ten) == 2
    assert next(ten) == 4
    assert next(ten) == 5
    assert next(ten) == 7
    assert next(ten) == 9
    assert next(ten) == 10
    assert next(ten) == 12
    assert next(ten) == 17
    assert next(ten) == 23
    assert next(ten) == 50


def test_pre_order_traversal_one_node(one_node_bst):
    """Test one node BST returns one val at a time.

    Uses 'pre order' order.
    """
    one = one_node_bst.pre_order()
    assert next(one) == 5


def test_pre_order_traversal_five_node(five_node_bst_with_tuple):
    """Test five node BST returns one val at a time.

    Uses 'pre order' order.
    """
    five = five_node_bst_with_tuple.pre_order()
    assert next(five) == 6
    assert next(five) == 4
    assert next(five) == 7
    assert next(five) == 6.5
    assert next(five) == 8


def test_pre_order_traversal_ten_node(ten_node_bst_with_list):
    """Test ten node BST returns one val at a time.

    Uses 'pre order' order.
    """
    ten = ten_node_bst_with_list.pre_order()
    assert next(ten) == 10
    assert next(ten) == 7
    assert next(ten) == 4
    assert next(ten) == 2
    assert next(ten) == 5
    assert next(ten) == 9
    assert next(ten) == 17
    assert next(ten) == 12
    assert next(ten) == 23
    assert next(ten) == 50


def test_post_order_traversal_one_node(one_node_bst):
    """Test one node BST returns one val at a time.

    Uses 'post order' order.
    """
    one = one_node_bst.post_order()
    assert next(one) == 5


def test_post_order_traversal_five_node(five_node_bst_with_tuple):
    """Test five node BST returns one val at a time.

    Uses 'post order' order.
    """
    five = five_node_bst_with_tuple.post_order()
    assert next(five) == 4
    assert next(five) == 6.5
    assert next(five) == 8
    assert next(five) == 7
    assert next(five) == 6


def test_post_order_traversal_ten_node(ten_node_bst_with_list):
    """Test ten node BST returns one val at a time.

    Uses 'post order' order.
    """
    ten = ten_node_bst_with_list.post_order()
    assert next(ten) == 2
    assert next(ten) == 5
    assert next(ten) == 4
    assert next(ten) == 9
    assert next(ten) == 7
    assert next(ten) == 12
    assert next(ten) == 50
    assert next(ten) == 23
    assert next(ten) == 17
    assert next(ten) == 10


def test_breadth_first_traversal_one_node(one_node_bst):
    """Test one node BST returns one val at a time.

    Uses breadth first order.
    """
    one = one_node_bst.breadth_first()
    assert next(one) == 5


def test_breadth_first_traversal_five_node(five_node_bst_with_tuple):
    """Test five node BST returns one val at a time.

    Uses breadth first order.
    """
    five = five_node_bst_with_tuple.breadth_first()
    assert next(five) == 6
    assert next(five) == 4
    assert next(five) == 7
    assert next(five) == 6.5
    assert next(five) == 8


def test_breadth_first_traversal_ten_node(ten_node_bst_with_list):
    """Test ten node BST returns one val at a time.

    Uses breadth first order.
    """
    ten = ten_node_bst_with_list.breadth_first()
    assert next(ten) == 10
    assert next(ten) == 7
    assert next(ten) == 17
    assert next(ten) == 4
    assert next(ten) == 9
    assert next(ten) == 12
    assert next(ten) == 23
    assert next(ten) == 2
    assert next(ten) == 5
    assert next(ten) == 50


def test_post_order_edge_case(five_node_edge_case):
    """Test to left child of right child bubble up edge case."""
    five = five_node_edge_case.post_order()
    assert next(five) == 2
    assert next(five) == 4
    assert next(five) == 6
    assert next(five) == 5
    assert next(five) == 3


def test_delete_on_five_node_bst(five_node_bst_with_tuple):
    """Test delete functionality on a five node BST once."""
    five_node = five_node_bst_with_tuple
    five_node.delete(8)
    assert five_node._root.right.val == 7




# =================================================


@pytest.fixture
def empty_tree():
    """Init empty tree fixture."""
    return BST()


@pytest.fixture
def tree_init_list():
    """Init with numbers 1-7 tree fixture."""
    return BST([4, 2, 3, 1, 6, 5, 7])


@pytest.fixture
def tree_init_list_shorter_list():
    """Init with nubers 1,3,4,6,7 tree fixture."""
    return BST([4, 3, 1, 6, 7])


@pytest.fixture
def tree_init_list_longer_list():
    """Init with number 1-7 tree fixture we need a differenct name."""
    return BST([4, 2, 3, 1, 6, 7, 5])


@pytest.fixture
def tree_init_one_node():
    """Init tree with one node."""
    tree = BST()
    tree.insert(3)
    return tree


@pytest.fixture
def tree_init_one_node_left():
    """Init binarySearch for del node 1 kid left."""
    return BST([4, 3])


@pytest.fixture
def tree_init_three_nodes_left():
    """Init binarySearch uneven."""
    return BST([4, 6, 5])


@pytest.fixture
def tree_init_three_nodes_right():
    """Init binarySearch uneven."""
    return BST([4, 5, 6])


@pytest.fixture
def tree_init_one_node_right():
    """Init binarySearch for del node 1 kid right."""
    return BST([2, 3])


@pytest.fixture
def imbalanced_left_tree():
    """Init imbalanced tree favoring left side."""
    return BST((7, 6, 5, 4, 3))


@pytest.fixture
def imbalanced_right_tree():
    """Init imbalanced tree favoring right side."""
    return BST((3, 4, 5, 6, 7))


def test_init_error_string():
    """Test init with string."""
    with pytest.raises(TypeError):
        BST('cake')


def test_init(empty_tree):
    """Test bst attributes with no data."""
    assert empty_tree.size() == 0
    assert empty_tree._rdepth == 0
    assert empty_tree._ldepth == 0
    assert empty_tree.depth() == 0
    assert empty_tree._root is None


def test_init_list_float():
    """Test init with iterable."""
    new_tree = BST(2.5)
    assert new_tree._root.val == 2.5
    assert new_tree.size() == 1
    assert new_tree._rdepth == 0
    assert new_tree._ldepth == 0
    assert new_tree.depth() == 0


def test_init_list():
    """Test init with iterable."""
    new_tree = BST([2, 1, 3])
    assert new_tree.size() == 3
    assert new_tree._rdepth == 1
    assert new_tree._ldepth == 1
    assert new_tree.depth() == 1


def test_init_tuple():
    """Test init with iterable."""
    new_tree = BST((2, 1, 3))
    assert new_tree.size() == 3
    assert new_tree._rdepth == 1
    assert new_tree._ldepth == 1
    assert new_tree.depth() == 1


def test_size():
    """Test size."""
    new_tree = BST()
    assert new_tree.size() == 0
    new_tree.insert(2)
    assert new_tree.size() == 1
    new_tree.insert(1)
    assert new_tree.size() == 2
    new_tree.insert(3)
    assert new_tree.size() == 3


def test_balance():
    """Test balance."""
    new_tree = BST()
    assert new_tree.balance() == 0
    new_tree.insert(2)
    assert new_tree.balance() == 0
    new_tree.insert(1)
    assert new_tree.balance() == -1
    new_tree.insert(3)
    assert new_tree.balance() == 0
    new_tree.insert(4)
    assert new_tree.balance() == 1


def test_depth():
    """Test depth."""
    new_tree = BST()
    assert new_tree.depth() == 0
    new_tree.insert(2)
    assert new_tree.depth() == 0
    new_tree.insert(1)
    assert new_tree.depth() == 1
    new_tree.insert(3)
    assert new_tree.depth() == 1
    new_tree.insert(4)
    assert new_tree.depth() == 2


def test_search():
    """Test search."""
    new_tree = BST()
    assert new_tree.search(2) is None
    new_tree.insert(2)
    assert new_tree.search(2).val == 2
    new_tree.insert(1)
    assert new_tree.search(1).val == 1
    new_tree.insert(3)
    assert new_tree.search(4) is None
    new_tree.insert(4)
    assert new_tree.search(4).val == 4


def test_contains():
    """Test contains method."""
    new_tree = BST()
    assert new_tree.contains(2) is False
    new_tree.insert(2)
    assert new_tree.contains(2) is True
    new_tree.insert(1)
    assert new_tree.contains(1) is True
    new_tree.insert(3)
    assert new_tree.contains(4) is False
    new_tree.insert(4)
    assert new_tree.contains(4) is True


def test_insert_tuple(empty_tree):
    """Test inserting tuple raises error."""
    with pytest.raises(TypeError):
        empty_tree.insert((9, 'hello'))


def test_insert_dupe(empty_tree):
    """Test insert."""
    empty_tree.insert(2)
    with pytest.raises(ValueError):
        empty_tree.insert(2)


def test_insert():
    """Test insert."""
    new_tree = BST()
    assert new_tree.contains(2) is False
    new_tree.insert(2)
    assert new_tree.contains(2) is True
    new_tree.insert(1)
    assert new_tree.contains(1) is True
    new_tree.insert(3)
    assert new_tree.contains(4) is False
    new_tree.insert(4)
    assert new_tree.contains(4) is True


def test_insert_depth(tree_init_three_nodes_left):
    """Test insert."""
    tree_init_three_nodes_left.delete(7)
    assert tree_init_three_nodes_left.depth() is 2


def test_breadth_first(tree_init_list):
    """Test breadth first."""
    gen = tree_init_list.breadth_first()
    assert next(gen) is 4
    assert next(gen) is 2
    assert next(gen) is 6
    assert next(gen) is 1
    assert next(gen) is 3
    assert next(gen) is 5
    assert next(gen) is 7


def test_pre_order(tree_init_list):
    """Test pre-order first."""
    gen = tree_init_list.pre_order()
    assert next(gen) is 4
    assert next(gen) is 2
    assert next(gen) is 1
    assert next(gen) is 3
    assert next(gen) is 6
    assert next(gen) is 5
    assert next(gen) is 7


def test_in_order(tree_init_list):
    """Test pre-order first."""
    gen = tree_init_list.in_order()
    assert next(gen) is 1
    assert next(gen) is 2
    assert next(gen) is 3
    assert next(gen) is 4
    assert next(gen) is 5
    assert next(gen) is 6
    assert next(gen) is 7


def test_post_order(tree_init_list):
    """Test pre-order first."""
    gen = tree_init_list.post_order()
    assert next(gen) is 1
    assert next(gen) is 3
    assert next(gen) is 2
    assert next(gen) is 5
    assert next(gen) is 7
    assert next(gen) is 6
    assert next(gen) is 4


def test_del_no_val(tree_init_list_longer_list):
    """Value error raised when delete called on value not in tree."""
    assert tree_init_list_longer_list.delete(10000) is None


def test_del_root_no_kids(tree_init_one_node):
    """Test del root when root has zero kids."""
    assert tree_init_one_node._root.val == 3
    tree_init_one_node.delete(3)
    assert tree_init_one_node._root is None


def test_del_node_left_kid(tree_init_three_nodes_left):
    """Test delete on node with one left child."""
    tree_init_three_nodes_left.delete(6)
    assert tree_init_three_nodes_left._root.val == 4
    assert tree_init_three_nodes_left._root.right.val == 5
    assert tree_init_three_nodes_left.depth() == 1
    assert tree_init_three_nodes_left.depth() == 1


def test_del_root_one_kid_right(tree_init_one_node_right):
    """Test del root when root has one right kids."""
    assert tree_init_one_node_right._root.right.val == 3
    assert tree_init_one_node_right._root.parent is None
    assert tree_init_one_node_right._root.right.parent.val == 2
    tree_init_one_node_right.delete(2)
    assert tree_init_one_node_right._root.right is None
    assert tree_init_one_node_right._root.val == 3
    assert tree_init_one_node_right._root.parent is None


def test_del_root_one_kid_left(tree_init_one_node_left):
    """Test del root when root has one left kids."""
    assert tree_init_one_node_left._root.left.val == 3
    tree_init_one_node_left.delete(4)
    assert tree_init_one_node_left._root.left is None
    assert tree_init_one_node_left._root.val == 3
    assert tree_init_one_node_left._root.parent is None


def test_del_left_node_check_parent(tree_init_list_longer_list):
    """Test to check if we reasigned parent."""
    tree_init_list_longer_list.delete(2)
    assert tree_init_list_longer_list.search(3).parent.val == 4
    tree_init_list_longer_list.delete(6)
    assert tree_init_list_longer_list.search(7).parent.val == 4


def test_del_2kids_node_check_parent(tree_init_list_shorter_list):
    """Test to check if we reasigned parent."""
    tree_init_list_shorter_list.delete(3)
    assert tree_init_list_shorter_list.search(1).parent.val == 4
    tree_init_list_shorter_list.delete(6)
    assert tree_init_list_shorter_list.search(7).parent.val == 4


def test_del_node_one_kid_right(tree_init_one_node_right):
    """Test del node when root has one right kids."""
    assert tree_init_one_node_right._root.right.val == 3
    tree_init_one_node_right.delete(3)
    assert tree_init_one_node_right._root.right is None
    assert tree_init_one_node_right._root.val == 2


def test_del_node_one_kid_left(tree_init_one_node_left):
    """Test del node when root has one left kids."""
    assert tree_init_one_node_left._root.left.val == 3
    tree_init_one_node_left.delete(3)
    assert tree_init_one_node_left._root.left is None
    assert tree_init_one_node_left._root.val == 4


def test_del_root_two_kids(tree_init_list):
    """Test del."""
    assert tree_init_list.contains(4)
    assert tree_init_list.size() is 7
    tree_init_list.delete(4)
    assert tree_init_list.size() is 6
    assert tree_init_list.contains(4) is False
    assert tree_init_list._root.val == 5
    assert tree_init_list._root.right.parent.val == 5
    assert tree_init_list._root.left.val == 2
    assert tree_init_list._root.right.val == 6
    assert tree_init_list._root.right.left is None
    assert tree_init_list.contains(7)
    tree_init_list.delete(7)
    assert tree_init_list.size() is 5
    assert tree_init_list.contains(7) is False
    assert tree_init_list.contains(6)
    tree_init_list.delete(6)
    assert tree_init_list.contains(6) is False


def test_del_left_node_two_kids(tree_init_list):
    """Test del node when has two  kids."""
    assert tree_init_list.contains(2)
    assert tree_init_list._root.val == 4
    assert tree_init_list.size() is 7
    tree_init_list.delete(2)
    assert tree_init_list.size() is 6
    assert tree_init_list.contains(2) is False
    assert tree_init_list._root.val == 4
    assert tree_init_list._root.left.val == 3
    assert tree_init_list._root.left.left.val == 1


def test_del_right_node_two_kids(tree_init_list):
    """Test del node when root has one right kids."""
    assert tree_init_list.contains(6)
    assert tree_init_list._root.val == 4
    assert tree_init_list.size() is 7
    tree_init_list.delete(6)
    assert tree_init_list.size() is 6
    assert tree_init_list.contains(6) is False
    assert tree_init_list._root.val == 4
    assert tree_init_list._root.right.val == 7
    assert tree_init_list._root.right.right is None


def test_del_right_branch(tree_init_list):
    """Test del on branch node right."""
    assert tree_init_list.contains(1)
    assert tree_init_list._root.val == 4
    tree_init_list.delete(1)
    assert tree_init_list.contains(1) is False
    assert tree_init_list.contains(2)
    assert tree_init_list.contains(3)
    assert tree_init_list._root.left.left is None


def test_del_left_branch(tree_init_list):
    """Test del on branch node left."""
    assert tree_init_list.contains(5)
    assert tree_init_list._root.val == 4
    tree_init_list.delete(5)
    assert tree_init_list.contains(5) is False
    assert tree_init_list.contains(6)
    assert tree_init_list.contains(7)
    assert tree_init_list._root.right.left is None


def test_del_rebalance(tree_init_list):
    """Test rebalance after delete."""
    assert tree_init_list._rdepth == 2
    assert tree_init_list._ldepth == 2
    assert tree_init_list.depth() == 2
    tree_init_list.delete(4)
    assert tree_init_list._rdepth == 2
    assert tree_init_list._ldepth == 2
    assert tree_init_list.depth() == 2
    tree_init_list.delete(7)
    assert tree_init_list._rdepth == 1
    assert tree_init_list._ldepth == 2
    assert tree_init_list.depth() == 2
    tree_init_list.delete(6)
    assert tree_init_list._rdepth == 0
    assert tree_init_list._ldepth == 2
    assert tree_init_list.depth() == 2
    tree_init_list.delete(1)
    tree_init_list.delete(3)
    assert tree_init_list._rdepth == 0
    assert tree_init_list._ldepth == 1
    assert tree_init_list.depth() == 1
    tree_init_list.delete(2)
    assert tree_init_list._rdepth == 0
    assert tree_init_list._ldepth == 0
    assert tree_init_list.depth() == 0


def test_del_rebalance_right(tree_init_three_nodes_right):
    """Test max depth on right-imbalanced tree."""
    tree_init_three_nodes_right.delete(6)
    assert tree_init_three_nodes_right.depth() is 1