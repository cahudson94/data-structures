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
def two_node_right_bst():
    """Two node BST to the right."""
    two = BST()
    two.insert(0)
    two.insert(1)
    return two


@pytest.fixture
def two_node_left_bst():
    """Two node BST to the left."""
    two = BST()
    two.insert(1)
    two.insert(0)
    return two


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
    five_node = BST((6, 3, 2, 5, 4))
    return five_node


@pytest.fixture
def six_node_range_0_to_5_bst():
    """Six nodes covering range zero to five."""
    b = BST([0, 1, 2, 3, 4, 5])
    return b


@pytest.fixture
def six_node_range_5_to_0_bst():
    """Six nodes covering range five to zero."""
    b = BST([5, 4, 3, 2, 1, 0])
    return b


@pytest.fixture
def six_node_right_heavy_bst():
    """Six node BST for edge cases."""
    b = BST([7, 5, 10, 8, 12, 32])
    return b


@pytest.fixture
def nine_node_with_succesor_children():
    """Nine node BST for edge cases."""
    b = BST([15, 13, 17, 14, 9, 30, 23, 12, 10])
    return b


@pytest.fixture
def ten_node_bst_with_list():
    """A BST initialized with ten nodes from list."""
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
    assert three_node_bst_with_list.balance() == 0


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
    assert five_node_bst_by_insert.balance() == 1


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
    gen = []
    for i in range(5):
        gen.append(next(five))
    assert gen == [4, 6, 6.5, 7, 8]


def test_in_order_traversal_ten_node(ten_node_bst_with_list):
    """Test ten node BST returns one val at a time.

    Uses 'in order' order.
    """
    ten = ten_node_bst_with_list.in_order()
    gen = []
    for i in range(10):
        gen.append(next(ten))
    assert gen == [2, 4, 5, 7, 9, 10, 12, 17, 23, 50]


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
    gen = []
    for i in range(5):
        gen.append(next(five))
    assert gen == [6, 4, 8, 7, 6.5]


def test_pre_order_traversal_ten_node(ten_node_bst_with_list):
    """Test ten node BST returns one val at a time.

    Uses 'pre order' order.
    """
    ten = ten_node_bst_with_list.pre_order()
    gen = []
    for i in range(10):
        gen.append(next(ten))
    assert gen == [10, 7, 4, 2, 5, 9, 12, 23, 17, 50]


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
    gen = []
    for i in range(5):
        gen.append(next(five))
    assert gen == [4, 6.5, 7, 8, 6]


def test_post_order_traversal_ten_node(ten_node_bst_with_list):
    """Test ten node BST returns one val at a time.

    Uses 'post order' order.
    """
    ten = ten_node_bst_with_list.post_order()
    gen = []
    for i in range(10):
        gen.append(next(ten))
    assert gen == [2, 5, 4, 9, 7, 17, 50, 23, 12, 10]


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
    gen = []
    for i in range(5):
        gen.append(next(five))
    assert gen == [6, 4, 8, 7, 6.5]


def test_breadth_first_traversal_ten_node(ten_node_bst_with_list):
    """Test ten node BST returns one val at a time.

    Uses breadth first order.
    """
    ten = ten_node_bst_with_list.breadth_first()
    gen = []
    for i in range(10):
        gen.append(next(ten))
    assert gen == [10, 7, 12, 4, 9, 23, 2, 5, 17, 50]


def test_post_order_edge_case(five_node_edge_case):
    """Test to left only tree traversal edge case post order."""
    five = five_node_edge_case.post_order()
    gen = []
    for i in range(5):
        gen.append(next(five))
    assert gen == [2, 4, 5, 3, 6]


def test_breadth_first_edge_case(five_node_edge_case):
    """Test to left only tree traversal edge case breadth first."""
    five = five_node_edge_case.breadth_first()
    gen = []
    for i in range(5):
        gen.append(next(five))
    assert gen == [6, 3, 2, 5, 4]


def test_in_order_edge_case(five_node_edge_case):
    """Test to left only tree traversal edge case in order."""
    five = five_node_edge_case.in_order()
    gen = []
    for i in range(5):
        gen.append(next(five))
    assert gen == [2, 3, 4, 5, 6]


def test_pre_order_edge_case(five_node_edge_case):
    """Test to left only tree traversal edge case pre order."""
    five = five_node_edge_case.pre_order()
    gen = []
    for i in range(5):
        gen.append(next(five))
    assert gen == [6, 3, 2, 5, 4]


def test_two_node_post_order_right(two_node_right_bst):
    """Test for traversal of a two node right BST via post order."""
    two = two_node_right_bst.post_order()
    gen = []
    for i in range(2):
        gen.append(next(two))
    assert gen == [1, 0]


def test_two_node_post_order_left(two_node_left_bst):
    """Test for traversal of a two node left BST via post order."""
    two = two_node_left_bst.post_order()
    gen = []
    for i in range(2):
        gen.append(next(two))
    assert gen == [0, 1]


def test_two_node_pre_order_right(two_node_right_bst):
    """Test for traversal of a two node right BST via pre order."""
    two = two_node_right_bst.pre_order()
    gen = []
    for i in range(2):
        gen.append(next(two))
    assert gen == [0, 1]


def test_two_node_pre_order_left(two_node_left_bst):
    """Test for traversal of a two node left BST via pre order."""
    two = two_node_left_bst.pre_order()
    gen = []
    for i in range(2):
        gen.append(next(two))
    assert gen == [1, 0]


def test_two_node_in_order_right(two_node_right_bst):
    """Test for traversal of a two node right BST via in order."""
    two = two_node_right_bst.in_order()
    gen = []
    for i in range(2):
        gen.append(next(two))
    assert gen == [0, 1]


def test_two_node_in_order_left(two_node_left_bst):
    """Test for traversal of a two node left BST via in order."""
    two = two_node_left_bst.in_order()
    gen = []
    for i in range(2):
        gen.append(next(two))
    assert gen == [0, 1]


def test_two_node_breadth_first_right(two_node_right_bst):
    """Test for traversal of a two node right BST via breadth first."""
    two = two_node_right_bst.breadth_first()
    gen = []
    for i in range(2):
        gen.append(next(two))
    assert gen == [0, 1]


def test_two_node_breadth_first_left(two_node_left_bst):
    """Test for traversal of a two node left BST via breadth first."""
    two = two_node_left_bst.breadth_first()
    gen = []
    for i in range(2):
        gen.append(next(two))
    assert gen == [1, 0]


def test_on_empty_bst_delete_returns_none(empty_bst):
    """Test deletion on empty BST."""
    assert empty_bst.delete(7) is None


def test_bad_data_delete_raises_error(empty_bst):
    """Test deletion of non int data."""
    with pytest.raises(TypeError):
        empty_bst.delete('lkj')


def test_delete_of_root_on_one_node_bst(one_node_bst):
    """Test deletion of single node BST."""
    one_node_bst.delete(5)
    assert one_node_bst._root is None


def test_delete_of_root_on_two_node_bst():
    """Test deletion of root on two node BST."""
    new_bst = BST([2, 5])
    new_bst.delete(2)
    assert new_bst._root.val == 5
    assert new_bst._length == 1
    assert new_bst.balance() == 0
    assert new_bst.depth() == 1


def test_delete_on_five_node_bst_with_tuple(five_node_bst_with_tuple):
    """Test delete functionality on a five node BST once."""
    five_node = five_node_bst_with_tuple
    five_node.delete(8)
    assert five_node._root.right.val == 7
    assert five_node.balance() == -1
    assert five_node.depth() == 3


def test_delete_head_on_five_node_bst_with_insert(five_node_bst_by_insert):
    """Test deletion of root changes root."""
    five_node_bst_by_insert.delete(6)
    assert five_node_bst_by_insert._root.val == 11


def test_delete_multiple_heads_on_five_node_bst(five_node_bst_by_insert):
    """Test deltion of root multiple times."""
    five_node_bst_by_insert.delete(6)
    assert five_node_bst_by_insert._root.val == 11
    assert five_node_bst_by_insert.depth() == 3
    five_node_bst_by_insert.delete(11)
    assert five_node_bst_by_insert._root.val == 2
    assert five_node_bst_by_insert.depth() == 2


def test_ten_node_delete_2_nodes(ten_node_bst_with_list):
    """Test deletion of two nodes from a ten node BST."""
    ten_node_bst_with_list.delete(9)
    assert ten_node_bst_with_list._length == 9
    ten_node_bst_with_list.delete(10)
    assert ten_node_bst_with_list._root.val == 7
    node7 = ten_node_bst_with_list.search(7)
    assert node7.right.val == 12
    assert node7.parent is None


def test_ten_node_delete_right_side(ten_node_bst_with_list):
    """Test deletion from right side only."""
    ten_node_bst_with_list.delete(23)
    assert ten_node_bst_with_list._root.right.right.val == 17


def test_delete_right_most_left_most_has_right_child():
    """Delete one child deletion test."""
    new_bst = BST([1, 5, 3, 10, 8, 6, 20, 7])
    assert new_bst.depth() == 6
    new_bst.delete(5)
    assert new_bst._root.right.val == 6
    assert new_bst.depth() == 5
    assert new_bst._root.right.right.val == 10


def test_multiple_deletes_on_more_robust_tree():
    """Test a BST with more nodes and full branches on both sides."""
    new_bst = BST([10, 2, 1, 9, 4, 3, 8, 6, 5, 7,
                   18, 11, 19, 16, 12, 17, 14, 13, 15])
    assert new_bst._root.val == 10
    new_bst.delete(16)
    assert new_bst._root.right.left.right.val == 15
    assert new_bst._root.right.left.right.left.val == 12
    new_bst.delete(11)
    assert new_bst._root.right.left.val == 15
    new_bst.delete(4)
    assert new_bst._root.left.right.left.val == 5
    assert new_bst.depth() == 7


def test_delete_leaf_of_root_small_tree(three_node_bst_with_list):
    """Test deletion of a leaf off the root."""
    b = three_node_bst_with_list
    assert b._root.val == 2
    assert b.size() == 3
    b.delete(2)
    assert b._root.val == 1
    assert b.size() == 2
    assert b.balance() == -1
    b.delete(3)
    assert b.balance() == 0
    assert b.depth() == 1


def test_delete_root_only_left_children(three_node_bst_with_list):
    """Test test deletion of left child only root."""
    b = three_node_bst_with_list
    assert b._root.val == 2
    assert b.size() == 3
    b.delete(3)
    assert b.size() == 2
    assert b.balance() == 1
    b.delete(2)
    assert b._root.val == 1
    assert b.balance() == 0
    assert b.depth() == 1
    b.delete(1)
    assert b.size() == 0
    assert b.depth() == 0


def test_delete_left_child_with_left_child():
    """Test deletion of left only child of a left child node."""
    b = BST([15, 12, 16, 10])
    b.delete(12)
    assert b._root.left.left is None
    assert b.size() == 3


def test_delete_right_child_with_right_child():
    """Test deletion of left only child of a left child node."""
    b = BST([8, 2, 10, 16])
    b.delete(10)
    assert b._root.right.right is None
    assert b.size() == 3


def test_delete_sub_tree_succesor_has_child(nine_node_with_succesor_children):
    """Test deletion of a sub tree root under the main root."""
    b = nine_node_with_succesor_children
    b.delete(13)
    assert b._root.left.val == 12
    assert b._root.left.right.val == 14
    assert b._root.left.left.right.val == 10


def test_delete_root_on_right_heavy_tree(six_node_right_heavy_bst):
    """Test deletion of the root when right is heavier."""
    b = six_node_right_heavy_bst
    b.delete(7)
    assert b._root.val == 5
    assert b.size() == 5


def test_delete_left_side_leaf(six_node_right_heavy_bst):
    """Test deletion of the root when right is heavier."""
    b = six_node_right_heavy_bst
    b.delete(8)
    assert b._root.right.left is None
    assert b.size() == 5


def test_blance_and_depth_of_wonky_bst(wonky_bst):
    """Test the balance of the wonky bst."""
    assert wonky_bst.balance() == 4
    assert wonky_bst.depth() == 9


def test_blance_and_depth_of_right_bst(right_side_bst):
    """Test the balance of the right bst."""
    assert right_side_bst.balance() == -6
    assert right_side_bst.depth() == 7


def test_blance_and_depth_of_left_bst(left_side_bst):
    """Test the balance of the left bst."""
    assert left_side_bst.balance() == 4
    assert left_side_bst.depth() == 5


def test_zero_to_five_range_root_del(six_node_range_0_to_5_bst):
    """Test deletion of root on six node tree at val 0."""
    b = six_node_range_0_to_5_bst
    b.delete(0)
    assert b._root.val == 1


def test_five_to_zero_range_root_del(six_node_range_5_to_0_bst):
    """Test deletion of root on six node tree at val 0."""
    b = six_node_range_5_to_0_bst
    b.delete(5)
    assert b._root.val == 4
