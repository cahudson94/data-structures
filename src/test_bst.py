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
    five_node = BST((6, 3, 2, 5, 4))
    return five_node


@pytest.fixture
def six_node_right_heavy_bst():
    """Six node BST for edge cases."""
    b = BST([10, 5, 12, 11, 1, 32])
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


def test_empty_bst_features(empty_bst):
    """Test base features of empty BST."""
    assert empty_bst._root is None
    assert empty_bst._length == 0
    assert empty_bst._depth == 0
    assert empty_bst._balance == 0


def test_empty_bstsize(empty_bst):
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


def test_search_with_badval_type(one_node_bst):
    """Test bad data on search raises error."""
    with pytest.raises(TypeError):
        one_node_bst.search('five')


def test_contains_with_badval_type(one_node_bst):
    """Test bad data on contains raises error."""
    with pytest.raises(TypeError):
        one_node_bst.contains('lskdfj')


def test_repeat_val_insert_attempt_fails(one_node_bst):
    """Test that insert an exisiting val returns None."""
    assert one_node_bst.insert(5) is None


def test_one_node_bst_val_is_root(one_node_bst):
    """Test that a BST with one node has root of one node."""
    assert one_node_bst._root.val == 5


def test_one_node_bst_correctsize(one_node_bst):
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


def test_three_node_bst_correctsize(three_node_bst):
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


def test_five_node_bst_correctsize(five_node_bst_with_tuple):
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


def test_ten_node_bst_correctsize(ten_node_bst_with_list):
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


def test_init_bst_raises_type_error_with_badval_in_list():
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


def test_in_order_traversal_edge_case():
    """Test for an in order traversal edge case."""
    b = BST([5, 4, 6, 3, 7])
    eight = b.in_order()
    assert next(eight) == 3
    assert next(eight) == 4
    assert next(eight) == 5
    assert next(eight) == 6
    assert next(eight) == 7


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


def test_post_order_traversal_edge_case():
    """Test for edge case with self balancing."""
    b = BST([7, 4, 8, 9, 3, 6, 5])
    seven = b.post_order()
    assert next(seven) == 3
    assert next(seven) == 5
    assert next(seven) == 6
    assert next(seven) == 4
    assert next(seven) == 9
    assert next(seven) == 8
    assert next(seven) == 7


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
    assert five_node.balance() == 1
    assert five_node.depth() == 3


def test_delete_head_on_five_node_bst_with_insert(five_node_bst_by_insert):
    """Test deletion of root changes root."""
    five_node_bst_by_insert.delete(6)
    assert five_node_bst_by_insert._root.val == 4.2


def test_delete_multiple_heads_on_five_node_bst(five_node_bst_by_insert):
    """Test deltion of root multiple times."""
    five_node_bst_by_insert.delete(6)
    assert five_node_bst_by_insert._root.val == 4.2
    assert five_node_bst_by_insert.depth() == 3
    five_node_bst_by_insert.delete(4.2)
    assert five_node_bst_by_insert._root.val == 2
    assert five_node_bst_by_insert.depth() == 2


def test_ten_node_delete_2_nodes(ten_node_bst_with_list):
    """Test deletion of two nodes from a ten node BST."""
    ten_node_bst_with_list.delete(9)
    assert ten_node_bst_with_list._length == 9
    ten_node_bst_with_list.delete(10)
    assert ten_node_bst_with_list._root.val == 7
    node7 = ten_node_bst_with_list.search(7)
    assert node7.right.val == 17
    assert node7.parent is None


def test_ten_node_delete_right_side(ten_node_bst_with_list):
    """Test deletion from right side only."""
    ten_node_bst_with_list.delete(17)
    assert ten_node_bst_with_list._root.right.right.val == 50


def test_delete_right_most_left_most_has_right_child():
    """Delete one child deletion test."""
    new_bst = BST([1, 5, 3, 10, 8, 6, 20, 7])
    assert new_bst.depth() == 4
    new_bst.delete(5)
    assert new_bst._root.val == 6
    assert new_bst._root.right.val == 8
    assert new_bst._root.right.left.val == 7


def test_multiple_deletes_on_more_robust_tree():
    """Test a BST with more nodes and full branches on both sides."""
    new_bst = BST([10, 2, 1, 9, 4, 3, 8, 6, 5, 7,
                   18, 11, 19, 16, 12, 17, 14, 13, 15])
    assert new_bst._root.val == 8
    new_bst.delete(16)
    assert new_bst._root.right.left.right.val == 12
    assert new_bst._root.right.right.val == 15
    new_bst.delete(11)
    assert new_bst._root.right.left.val == 10
    new_bst.delete(4)
    assert new_bst._root.left.right.left.val == 5
    assert new_bst.depth() == 5


def test_delete_leaf_of_root_small_tree(three_node_bst_with_list):
    """Test deletion of a leaf off the root."""
    b = three_node_bst_with_list
    assert b._root.val == 2
    assert b.size() == 3
    b.delete(2)
    assert b._root.val == 1
    assert b.size() == 2
    assert b.balance() == 1
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
    assert b.balance() == -1
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


def test_delete_right_child_with_left_child():
    """Test deletion of left only child of a right child node."""
    b = BST([4, 2, 8, 1, 3, 6, 9, 8.5])
    assert b._root.right.right.val == 9
    b.delete(9)
    assert b._root.right.right.val == 8.5
    assert b.size() == 7


def test_delete_right_child_with_right_child():
    """Test deletion of left only child of a left child node."""
    b = BST([8, 2, 10, 16])
    b.delete(10)
    assert b._root.right.right is None
    assert b.size() == 3


def test_delete_left_child_with_right_child():
    """Test deletion of left only child of a right child node."""
    b = BST([6, 5, 9, 3, 8, 12, 5.5, 4])
    assert b._root.left.left.val == 3
    b.delete(3)
    assert b._root.left.left.val == 4
    assert b.size() == 7


def test_delete_sub_tree_succesor_has_child(nine_node_with_succesor_children):
    """Test deletion of a sub tree root under the main root."""
    b = nine_node_with_succesor_children
    b.delete(13)
    assert b._root.left.val == 12
    assert b._root.left.right.val == 14
    assert b._root.left.left.val == 10


def test_delete_root_on_right_heavy_left_sub_tree():
    """Test deletion of the root when right is heavier."""
    b = BST([14, 8, 16, 9, 7, 18, 8.5, 12])
    b.delete(8)
    assert b._root.left.val == 8.5
    assert b._root.left.left.val == 7
    assert b.size() == 7


def test_delete_left_side_leaf(six_node_right_heavy_bst):
    """Test deletion of the root when right is heavier."""
    b = six_node_right_heavy_bst
    b.delete(11)
    assert b._root.right.left is None
    assert b.size() == 5


def test_delete_right_side_leaf_small():
    """Test deletion of a right leaf off the root."""
    b = BST([2, 3, 1])
    b.delete(3)
    assert b._root.right is None
    assert b.size() == 2


def test_delete_left_side_leaf_small():
    """Test deletion of a left leaf off the root."""
    b = BST([2, 3, 1])
    b.delete(1)
    assert b._root.left is None
    assert b.size() == 2






@pytest.fixture
def bst_empty():
    """Create a binary search tree."""
    from bst import BST
    return BST()


@pytest.fixture
def bst_all_to_left():
    r"""Create a binary search tree 5 numbers snake.
                  4
                 /  \
                2    5
               / \
              1   3
    depth: 3
    balance: -1
    === Search Transversals ===
    in_order: (1, 2, 3, 4, 5)
    pre_order: (4, 2, 1, 3, 5)
    breadth_first: (4, 2, 5, 1, 3)
    post_order: (1, 3, 2, 5, 4)
    """
    from bst import BST
    return BST([5, 4, 1, 3, 2])


@pytest.fixture
def bst_balanced():
    r"""Create a binary search tree 5 numbers.
                     5
                   /   \
                  2     6
                 / \     \
                1   3     7
    depth: 3
    balance: 0
    === Search Transversals ===
    in_order: (1, 2, 3, 5, 6, 7)
    pre_order: (5, 2, 1, 3, 6, 7)
    breadth_first: (5, 2, 6, 1, 3, 7)
    post_order: (1, 3, 2, 7, 6, 5)
    """
    from bst import BST
    return BST([5, 6, 2, 3, 1, 7])


@pytest.fixture
def bst_right_balance():
    r"""Create a binary search tree 5 numbers.
                     6
                   /   \
                  5     8
                 /     / \
                2     7   9
    depth: 3
    balance: 0
    === Search Transversals ===
    in_order: (2, 5, 6, 8, 7, 9)
    pre_order: (6, 5, 2, 8, 7, 9)
    breadth_first: (6, 5, 8, 2, 7, 9)
    post_order: (2, 5, 7, 9, 8, 6)
    """
    from bst import BST
    return BST([5, 8, 6, 9, 2, 7])


@pytest.fixture
def bst_100_rand():
    """100 random numbers in bst."""
    from bst import BST
    from random import shuffle
    rando = [num for num in range(100)]
    shuffle(rando)
    tree = BST(rando)
    return tree


@pytest.fixture
def bst_wiki():
    r"""Wikipedia's example tree structure.
                      7
                   /     \
                  4       9
                /   \    /
              2      6   8
            /  \    /
           1    3  5
    depth: 4
    balance: -1
    === Search Transversals ===
    in_order: (1, 2, 3, 4, 5, 6, 7, 8, 9)
    pre_order: (7, 4, 2, 1, 3, 6, 5, 9, 8)
    breadth_first: (7, 4, 9, 2, 6, 8, 1, 3, 5)
    post_order: (1, 3, 2, 5, 6, 4, 8, 9, 7)
    """
    from bst import BST
    tree = BST([6, 7, 9, 8, 2, 1, 4, 3, 5])
    return tree


@pytest.fixture
def three():
    """Create three item tree."""
    from bst import BST
    tree = BST([2, 1, 3])
    return tree


@pytest.fixture
def comp():
    r"""Create Large binary tree.
                          11
                      /        \
                    8           13
                  /   \        /  \
                6     10     12    14
               / \    /              \
              4   7  9                15
    in_order (4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
    pre_order: (11, 8, 6, 4, 7, 10, 9, 13, 12, 14, 15)
    breadth_first: (11, 8, 13, 6, 10, 12, 14, 4, 7, 9, 15)
    post_order: (4, 7, 6, 9, 10, 8, 12, 15, 14, 13, 11)
    """
    from bst import BST
    return BST([10, 6, 4, 8, 7, 9, 13, 11, 14, 12, 15])


@pytest.fixture
def right_left_most_has_right_child():
    r"""Large binary tree.
                     5
                    /  \
                   3    8
                  /    /  \
                 1    6    10
                       \     \
                       7     20
    in_order (1, 3, 5, 6, 7, 8, 10, 20)
    pre_order: (5, 3, 1, 8, 6, 7, 10, 20)
    breadth_first: (5, 3, 8, 1, 6, 10, 7, 20)
    post_order: (1, 3, 7, 6, 20, 10, 8, 5)
    """
    from bst import BST
    return BST([1, 5, 3, 10, 8, 6, 20, 7])


@pytest.fixture
def robust():
    r"""More robust tree.
                     8
                /        \
             4            13
           /   \        /    \
         2      6      11     16
        / \     /\     /\    /   \
       1   3   5  7  10 12   14   18
                     /        \   / \
                    9         15 17  19
    Is Robust.
    """
    from bst import BST
    return BST([
        10, 2, 1, 9, 4, 3, 8, 6, 5, 7, 18, 11, 19, 16, 12, 17, 14, 13, 15
    ])


@pytest.fixture
def hard_mode():
    r"""Test The First Rule of Hard Mode.
                     20
                   /    \
                  5      40
                /  \    /   \
               3   10  30   45
                   /  /  \    \
                  8  25  35    50
                         /
                        33
    in_order: (3, 5, 8, 10, 20, 25, 30, 33, 35, 40, 45, 50)
    breadth_first: (20, 5, 40, 3, 10, 30, 45, 8, 25, 35, 50, 33)
    Try and delete 3!
                     30
                   /    \
                  20    40
                /  \   /  \
               8   25 35  45
              / \     /     \
             5  10   33      50
    in_order: (4, 8, 10, 20, 25, 30, 33, 35, 40, 45, 50)
    breadth_first: (30, 20, 40, 8, 25, 35, 45, 5, 10, 33, 50)
    """
    from bst import BST
    return BST([
        20, 5, 40, 3, 10, 30, 45, 8, 25, 35, 50, 33
    ])


@pytest.fixture
def three_del():
    """Test Simple balanced three for base of tests."""
    from bst import BST
    return BST([10, 20, 30])


def test_initalizing_with_non_iterable_or_not_numbers_raises_ValueError():
    """Init returns Value error with with non-numbers or non-iterables."""
    from bst import BST
    with pytest.raises(TypeError):
        BST("dfsdfadgasdg")


def test_insert_must_be_a_number(bst_empty):
    """Raise TypeError on non number insert."""
    with pytest.raises(TypeError):
        bst_empty.insert("dfsdfadgasdg")


def test_insert_to_empty_tree_increases_tree_length(bst_empty):
    """Insert increses length."""
    bst_empty.insert(1)
    assert len(bst_empty) == 1


def test_insert_adds_value_to_tree(bst_balanced):
    """Value added to tree."""
    bst_balanced.insert(15)
    assert bst_balanced.contains(15) is True
    assert bst_balanced.search(15).val == 15


def test_insert_will_not_duplicate_value(bst_balanced):
    """Value not added twice."""
    bst_balanced.insert(6)
    assert bst_balanced.size() == 6


def test_insert_to_balanced_tree_changes_balance(bst_balanced):
    """Balance changes."""
    assert bst_balanced.balance() == 0
    bst_balanced.insert(4)
    assert bst_balanced.balance() == -1


def test_search_finds_node(bst_balanced):
    """Search returns node with value."""
    assert bst_balanced.search(1).val == 1


def test_search_returns_none_when_value_not_in_tree_right(bst_balanced):
    """Search returns None."""
    assert bst_balanced.search(25) is None


def test_search_returns_none_when_value_notin_tree_left(bst_all_to_left):
    """Catch case value less than tree values."""
    assert bst_all_to_left.search(0) is None


def test_size_is_correct_on_empty_tree(bst_empty):
    """Tree size is accurate."""
    assert bst_empty.size() == 0


def test_size_is_correct_on_filled_tree(bst_100_rand):
    """Tree size is accurate."""
    assert bst_100_rand.size() == 100


def test_depth_returns_zero_on_empty_tree(bst_empty):
    """Return 0 on empty tree."""
    assert bst_empty.depth() == 0


def test_depth_returns_correct_value_balanced_tree(bst_balanced):
    """Return value on tree."""
    assert bst_balanced.depth() == 3


def test_depth_returns_correct_value_right_balanced_tree(bst_right_balance):
    """Return value on empty tree."""
    assert bst_right_balance.depth() == 3


def test_depth_returns_correct_value_left_balanced_tree(bst_all_to_left):
    """Return value on empty tree."""
    assert bst_all_to_left.depth() == 3


def test_contains_returns_false_on_empty_tree(bst_empty):
    """False on empty tree."""
    assert bst_empty.contains(4) is False


def test_contains_returns_false_on_balanced_tree(bst_balanced):
    """False on balanced tree."""
    assert bst_balanced.contains(25) is False


def test_contains_returns_false_on_right_balanced_tree(bst_right_balance):
    """False on right balanced tree."""
    assert bst_right_balance.contains(25) is False


def test_contains_returns_false_on_left_balanced_tree(bst_all_to_left):
    """False on left balanced tree."""
    assert bst_all_to_left.contains(25) is False


def test_contains_returns_true_on_tree_with_value_left(bst_all_to_left):
    """Tree has value true."""
    assert bst_all_to_left.contains(3) is True
    assert bst_all_to_left.contains(1) is True
    assert bst_all_to_left.contains(2) is True


def test_contains_returns_true_on_tree_with_value_right(bst_right_balance):
    """Tree has value true."""
    assert bst_right_balance.contains(6) is True
    assert bst_right_balance.contains(2) is True


def test_contains_returns_true_on_tree_with_value(bst_balanced):
    """Tree has value true."""
    assert bst_balanced.contains(6) is True
    assert bst_balanced.contains(3) is True


def test_balance_right_tree(bst_right_balance):
    """Tree balanced right returns 2."""
    assert bst_right_balance.balance() == 0


def test_balance_left_tree(bst_all_to_left):
    """Tree balanced right returns -1."""
    assert bst_all_to_left.balance() == -1


def test_balance_balanced_tree(bst_balanced):
    """Tree balanced right returns 0."""
    assert bst_balanced.balance() == 0


def test_balance_empty_tree(bst_empty):
    """Tree balanced right returns 0."""
    assert bst_empty.balance() == 0


# =============== Beefy Re-balance Tests ================ #


def test_random_100_balance_remains_between_1_and_negative_1(bst_100_rand):
    """Test random 100 balance between 1 and -1."""
    assert bst_100_rand.balance() in range(-1, 2)


def test_straight_100_balance_remains_between_1and_negative_1():
    """Test 100 numbers in a row still has balance."""
    from bst import BST
    tree = BST(x for x in range(100))
    assert tree.balance() in range(-1, 2)


def test_backwards_100_balance_remains_between_1_and_negative_1():
    """Test 100 numbers in a row still has balance."""
    from bst import BST
    tree = BST([x for x in range(100)][::-1])
    assert tree.balance() in range(-1, 2)


def test_rand_100_depth_remains_less_than_8():
    """Test 100 numbers depth rational."""
    from bst import BST
    from random import shuffle
    max_depth = 0
    for x in range(10):
        rando = [x for x in range(100)]
        shuffle(rando)
        tree = BST(rando)
        tree_depth = tree.depth()
        if tree_depth > max_depth:
            max_depth = tree_depth
    assert max_depth == 8


# =================== Transversal Tests ================== #


def test_in_order_0_0(bst_empty):
    """Test in order Transversal with various tress."""
    assert tuple(bst_empty.in_order()) == ()


def test_in_order_one_item_tree(bst_empty):
    """Test in order works on one item tree."""
    bst_empty.insert(10)
    assert next(bst_empty.in_order()) == 10


def test_in_order_0_1(bst_balanced):
    """Test in order Transversal with various tress."""
    assert tuple(bst_balanced.in_order()) == (1, 2, 3, 5, 6, 7)


def test_in_order_0_2(bst_all_to_left):
    """Test in order Transversal with various tress."""
    assert tuple(bst_all_to_left.in_order()) == (1, 2, 3, 4, 5)


def test_in_order_0_3(bst_right_balance):
    """Test in order Transversal with various tress."""
    assert tuple(bst_right_balance.in_order()) == (2, 5, 6, 7, 8, 9)


def test_random_100_in_order(bst_100_rand):
    """Test random 100 retains in_order transversal."""
    assert tuple(bst_100_rand.in_order()) == tuple(x for x in range(100))


def testin_order_0_4(bst_wiki):
    """Test in order Transversal with various tress."""
    assert tuple(bst_wiki.in_order()) == (1, 2, 3, 4, 5, 6, 7, 8, 9)


def test_pre_order_0_0(bst_empty):
    """Test pre order Transversal with various tress."""
    assert tuple(bst_empty.pre_order()) == ()


def test_pre_order_0_1(bst_balanced):
    """Test pre order Transversal with various tress."""
    assert tuple(bst_balanced.pre_order()) == (5, 2, 1, 3, 6, 7)


def test_pre_order_0_2(bst_all_to_left):
    """Test pre order Transversal with various tress."""
    assert tuple(bst_all_to_left.pre_order()) == (4, 2, 1, 3, 5)


def test_pre_order_0_3(bst_right_balance):
    """Test pre order Transversal with various tress."""
    assert tuple(bst_right_balance.pre_order()) == (6, 5, 2, 8, 7, 9)


def test_pre_order_0_4(bst_wiki):
    """Test pre order Transversal with various tress."""
    assert tuple(bst_wiki.pre_order()) == (7, 4, 2, 1, 3, 6, 5, 9, 8)


def test_post_order_0_0(bst_empty):
    """Test post_order Transversal with various tress."""
    assert tuple(bst_empty.post_order()) == ()


def test_post_order_0_1(bst_balanced):
    """Test post_order Transversal with various tress."""
    assert tuple(bst_balanced.post_order()) == (1, 3, 2, 7, 6, 5)


def test_post_order_0_2(bst_all_to_left):
    """Test post_order Transversal with various tress."""
    assert tuple(bst_all_to_left.post_order()) == (1, 3, 2, 5, 4)


def test_post_order_0_3(bst_right_balance):
    """Test post_order Transversal with various tress."""
    assert tuple(bst_right_balance.post_order()) == (2, 5, 7, 9, 8, 6)


def test_post_order_0_4(bst_wiki):
    """Test post_order Transversal with various tress."""
    assert tuple(bst_wiki.post_order()) == (1, 3, 2, 5, 6, 4, 8, 9, 7)


def test_breadth_first_0_0(bst_empty):
    """Test breadth_first Transversal with various tress."""
    assert tuple(bst_empty.breadth_first()) == ()


def test_breadth_first_0_1(bst_balanced):
    """Test breadth_first Transversal with various tress."""
    assert tuple(bst_balanced.breadth_first()) == (5, 2, 6, 1, 3, 7)


def test_breadth_first_0_2(bst_all_to_left):
    """Test breadth_first Transversal with various tress."""
    assert tuple(bst_all_to_left.breadth_first()) == (4, 2, 5, 1, 3)


def test_breadth_first_0_3(bst_right_balance):
    """Test breadth_first Transversal with various tress."""
    assert tuple(bst_right_balance.breadth_first()) == (6, 5, 8, 2, 7, 9)


def test_breadth_first_0_4(bst_wiki):
    """Test breadth_first Transversal with various tress."""
    assert tuple(bst_wiki.breadth_first()) == (7, 4, 9, 2, 6, 8, 1, 3, 5)


# ===================  Delete Tests ===================== #


def test_delete_empty_bst(bst_empty):
    """Delete returns none on empty tree. Tree remains."""
    assert bst_empty.delete() is None
    assert bst_empty._root is None


def test_delete_empty_bst_value_not_in_tree(bst_empty):
    """Test delete on empty tree with value not in tree."""
    assert bst_empty.delete(5) is None
    assert bst_empty._root is None


def test_four_nodes_needs_right_rotation(three_del):
    """Test delete requires right rotation."""
    three_del.insert(5)
    three_del.delete(30)
    assert tuple(three_del.in_order()) == (5, 10, 20)
    assert tuple(three_del.breadth_first()) == (10, 5, 20)


def test_four_nodes_needs_left_rotation(three_del):
    """Test four node with deletion requireing left rotation."""
    three_del.insert(40)
    three_del.delete(10)
    assert tuple(three_del.in_order()) == (20, 30, 40)
    assert tuple(three_del.breadth_first()) == (30, 20, 40)


def test_four_nodes_needs_right_left_rotation(three_del):
    """Test right left delete rotation."""
    three_del.insert(25)
    three_del.delete(10)
    assert tuple(three_del.in_order()) == (20, 25, 30)
    assert tuple(three_del.breadth_first()) == (25, 20, 30)


def test_four_nodes_needs_left_right_rotation(three_del):
    """Test right left delete rotation."""
    three_del.insert(15)
    three_del.delete(30)
    assert tuple(three_del.in_order()) == (10, 15, 20)
    assert tuple(three_del.breadth_first()) == (15, 10, 20)


def test_delete_right_leaf_no_rotation(bst_balanced):
    """Test normal deletion, no rotation."""
    bst_balanced.delete(7)
    assert tuple(bst_balanced.in_order()) == (1, 2, 3, 5, 6)
    assert tuple(bst_balanced.breadth_first()) == (5, 2, 6, 1, 3)


def test_delete_left_leaf_no_rotation(bst_balanced):
    """Test normal deletion, no rotation."""
    bst_balanced.delete(1)
    assert tuple(bst_balanced.in_order()) == (2, 3, 5, 6, 7)
    assert tuple(bst_balanced.breadth_first()) == (5, 2, 6, 3, 7)


def test_delete_right_branch_no_rotation(bst_balanced):
    """Test normal deletion, no rotation."""
    bst_balanced.delete(6)
    assert tuple(bst_balanced.in_order()) == (1, 2, 3, 5, 7)
    assert tuple(bst_balanced.breadth_first()) == (5, 2, 7, 1, 3)


def test_delete_left_branch_no_rotation(bst_balanced):
    """Test normal deletion, no rotation."""
    bst_balanced.delete(2)
    assert tuple(bst_balanced.in_order()) == (1, 3, 5, 6, 7)
    assert tuple(bst_balanced.breadth_first()) == (5, 3, 6, 1, 7)


def test_delele_requires_right_branch_rotation(comp):
    """Test delete leaf, branch needs right rotation."""
    comp.delete(12)
    assert tuple(comp.in_order()) == (4, 6, 7, 8, 9, 10, 11, 13, 14, 15)
    assert tuple(comp.breadth_first()) == (11, 8, 14, 6, 10, 13, 15, 4, 7, 9)


# Bugger bug below.
def test_del_right_left_most_has_right(right_left_most_has_right_child):
    """Delete one child deletion test."""
    right_left_most_has_right_child.delete(5)
    assert tuple(right_left_most_has_right_child.in_order()) == (
        1, 3, 6, 7, 8, 10, 20
    )


def test_handle_root_deletion(right_left_most_has_right_child):
    """Remove root retains tree."""
    right_left_most_has_right_child.delete(1)
    assert tuple(right_left_most_has_right_child.in_order()) == (
        3, 5, 6, 7, 8, 10, 20
    )


def test_delete_retains_depth(comp):
    """Depth correnctly retained through series of deletions."""
    assert comp.depth() == 4
    comp.delete(7)
    assert tuple(comp.in_order()) == (4, 6, 8, 9, 10, 11, 12, 13, 14, 15)
    comp.delete(9)
    assert comp.depth() == 4
    comp.delete(4)
    comp.delete(15)
    assert comp.depth() == 3
    comp.delete(6)
    comp.delete(10)
    assert comp.depth() == 3
    comp.delete(12)
    comp.delete(14)
    assert comp.depth() == 2
    comp.delete(13)
    assert comp.depth() == 2
    assert tuple(comp.in_order()) == (8, 11)
    comp.delete(11)
    assert next(comp.in_order()) == 8
    assert comp.depth() == 1
    comp.delete(8)
    assert comp.depth() == 0
    comp.delete(12)
    assert comp.depth() == 0


def test_balance_value(comp):
    """Balance value correnctly tracked through series of deletions."""
    assert comp.balance() == 0
    comp.delete(7)
    comp.delete(9)
    comp.delete(15)
    assert comp.balance() == -1
    comp.delete(4)
    assert comp.balance() == 0
    comp.delete(12)
    assert comp.balance() == 0
    comp.delete(14)
    assert comp.balance() == -1
    comp.delete(6)
    comp.delete(10)
    assert comp.balance() == 0
    comp.delete(8)
    assert comp.balance() == 1
    comp.delete(13)
    assert comp.balance() == 0
    comp.delete(11)
    assert comp.balance() == 0


def test_delete_node_empty_returns_none(bst_empty):
    """Test delete with empty bst."""
    assert bst_empty.delete(5) is None


def test_delete_on_empty_bst_leaves_bst_intact(bst_empty):
    """Pretty verbose test name."""
    bst_empty.delete(1)
    assert bst_empty._root is None


def test_delete_tree_with_one_node_leaves_empty_tree(bst_empty):
    """Delete single node."""
    bst_empty.insert(1)
    bst_empty.delete(1)
    assert bst_empty._root is None
    with pytest.raises(AttributeError):
        bst_empty._root.val
    assert bst_empty.size() == 0


def test_delete_two_node_left_balanced_tree_01(bst_empty):
    """Delete root node shifts other node."""
    bst_empty.insert(2)
    bst_empty.insert(1)
    bst_empty.delete(2)
    assert bst_empty._root.val == 1
    assert bst_empty._root.left is None


def test_delete_two_node_left_balanced_tree_02(bst_empty):
    """Delete last node leaves one node tree."""
    bst_empty.insert(2)
    bst_empty.insert(1)
    assert bst_empty._root.val == 2
    assert tuple(bst_empty.in_order()) == (1, 2)
    assert tuple(bst_empty.breadth_first()) == (2, 1)
    bst_empty.delete(1)
    assert bst_empty._root.val == 2
    assert bst_empty._root.right is None
    assert bst_empty._root.left is None
    assert len(bst_empty) == 1


def test_delete_left_tree_single_child(bst_all_to_left):
    """One child deletion test."""
    bst_all_to_left.delete(4)
    assert bst_all_to_left.search(3).val == 3
    assert bst_all_to_left.search(4) is None


def test_delete_two_node_right_balanced_tree_01(bst_empty):
    """Delete root node shifts other node."""
    bst_empty.insert(1)
    bst_empty.insert(3)
    bst_empty.delete(1)
    assert bst_empty._root.val == 3
    assert bst_empty._root.left is None
    assert bst_empty._root.right is None


def test_delete_two_node_right_balanced_tree_02(bst_empty):
    """Delete last node leaves one node tree."""
    bst_empty.insert(1)
    bst_empty.insert(3)
    bst_empty.delete(3)
    assert bst_empty._root.val == 1
    assert bst_empty._root.right is None
    assert bst_empty._root.left is None
    assert len(bst_empty) == 1


def test_delete_three_node_tree_01(three):
    """Delete route node leaves tree in correct order."""
    three.delete(2)
    assert three._root.val == 3
    assert three._root.right is None
    assert three._root.left.val == 1
    assert tuple(three.in_order()) == (1, 3)


def test_delete_three_node_tree_02(three):
    """Delete left node leaves tree in order."""
    three.delete(1)
    assert three._root.val == 2
    assert three._root.right.val == 3
    assert three._root.left is None
    assert tuple(three.in_order()) == (2, 3)


def test_delete_three_node_tree_03(three):
    """Delete right node leaves tree in order."""
    three.delete(3)
    assert three._root.val == 2
    assert three._root.right is None
    assert three._root.left.val == 1
    assert tuple(three.in_order()) == (1, 2)


def test_delete_complex_tree_01(comp):
    """Delete route 10."""
    comp.delete(10)
    assert tuple(comp.in_order()) == (4, 6, 7, 8, 9, 11, 12, 13, 14, 15)
    assert tuple(comp.breadth_first()) == (11, 8, 13, 6, 9, 12, 14, 4, 7, 15)


def test_delete_complex_tree_02(comp):
    """Delete left most 4."""
    comp.delete(4)
    assert tuple(comp.in_order()) == (6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
    assert tuple(comp.breadth_first()) == (11, 8, 13, 6, 10, 12, 14, 7, 9, 15)


def test_delete_complex_tree_03(comp):
    """Delete right most 15."""
    comp.delete(15)
    assert tuple(comp.in_order()) == (4, 6, 7, 8, 9, 10, 11, 12, 13, 14)
    assert tuple(comp.breadth_first()) == (11, 8, 13, 6, 10, 12, 14, 4, 7, 9)


def test_delete_complex_tree_04(comp):
    """Delete mid right 13."""
    comp.delete(13)
    assert tuple(comp.in_order()) == (4, 6, 7, 8, 9, 10, 11, 12, 14, 15)
    assert tuple(comp.breadth_first()) == (11, 8, 14, 6, 10, 12, 15, 4, 7, 9)


def test_delete_complex_tree_05(comp):
    """Delete mid left 8."""
    comp.delete(8)
    assert tuple(comp.in_order()) == (4, 6, 7, 9, 10, 11, 12, 13, 14, 15)
    assert tuple(comp.breadth_first()) == (11, 9, 13, 6, 10, 12, 14, 4, 7, 15)


def test_delete_complex_tree_06(comp):
    """Delete bottom left 9."""
    comp.delete(9)
    assert tuple(comp.in_order()) == (4, 6, 7, 8, 10, 11, 12, 13, 14, 15)
    assert tuple(comp.breadth_first()) == (11, 8, 13, 6, 10, 12, 14, 4, 7, 15)


def test_delete_complex_tree_07(comp):
    """Delete bottom right 12."""
    comp.delete(12)
    assert tuple(comp.in_order()) == (4, 6, 7, 8, 9, 10, 11, 13, 14, 15)
    assert tuple(comp.breadth_first()) == (11, 8, 14, 6, 10, 13, 15, 4, 7, 9)


def test_delete_complex_tree_08(comp):
    """Delete mid bottom right 11."""
    comp.delete(11)
    assert tuple(comp.in_order()) == (4, 6, 7, 8, 9, 10, 12, 13, 14, 15)
    assert tuple(comp.breadth_first()) == (12, 8, 14, 6, 10, 13, 15, 4, 7, 9)


def test_del_handles_multiple_place_changes(robust):
    """Delete a node that requires multiple changes to correct."""
    robust.delete(9)
    assert robust.balance() == 1
    assert tuple(robust.in_order()) == (
        1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
    )
    robust.delete(10)
    assert tuple(robust.in_order()) == (
        1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18, 19
    )
    assert robust.balance() == 1
    assert robust.depth() == 5
    robust.delete(19)
    robust.delete(11)
    robust.delete(12)
    assert tuple(robust.in_order()) == (
        1, 2, 3, 4, 5, 6, 7, 8, 13, 14, 15, 16, 17, 18
    )
    assert tuple(robust.breadth_first()) == (
        8, 4, 16, 2, 6, 14, 18, 1, 3, 5, 7, 13, 15, 17
    )
    assert robust.balance() == 0
    assert robust.depth() == 4


def test_hard_mode(hard_mode):
    """Is hard mode."""
    assert tuple(hard_mode.in_order()) == (
        3, 5, 8, 10, 20, 25, 30, 33, 35, 40, 45, 50
    )
    assert tuple(hard_mode.breadth_first()) == (
        20, 5, 40, 3, 10, 30, 45, 8, 25, 35, 50, 33
    )
    hard_mode.delete(3)
    assert tuple(hard_mode.in_order()) == (
        5, 8, 10, 20, 25, 30, 33, 35, 40, 45, 50
    )
    # Hard Mode True test Below!!!
    assert tuple(hard_mode.breadth_first()) == (
        30, 20, 40, 8, 25, 35, 45, 5, 10, 33, 50
    )


# =============== AVL Testing ====================#

def test_right_rotation_three_node_tree_including_root():
    """Test three nodes rotate right."""
    from bst import BST
    tree = BST([5, 4, 3])
    assert tuple(tree.in_order()) == (3, 4, 5)
    assert tuple(tree.breadth_first()) == (4, 3, 5)
    assert tuple(tree.pre_order()) == (4, 3, 5)
    assert tuple(tree.post_order()) == (3, 5, 4)
    assert tree.depth() == 2
    assert tree.balance() == 0


def test_left_rotation_three_node_tree_including_root():
    """Test three nodes rotate right."""
    from bst import BST
    tree = BST([3, 4, 5])
    assert tuple(tree.in_order()) == (3, 4, 5)
    assert tuple(tree.breadth_first()) == (4, 3, 5)
    assert tuple(tree.pre_order()) == (4, 3, 5)
    assert tuple(tree.post_order()) == (3, 5, 4)
    assert tree.depth() == 2
    assert tree.balance() == 0


def test_right_rotation_four_node_tree():
    """Test four nodes rotate right, no root change."""
    from bst import BST
    tree = BST([5, 4, 3, 2, 1])
    assert tuple(tree.in_order()) == (1, 2, 3, 4, 5)
    assert tuple(tree.breadth_first()) == (4, 2, 5, 1, 3)
    assert tuple(tree.pre_order()) == (4, 2, 1, 3, 5)
    assert tuple(tree.post_order()) == (1, 3, 2, 5, 4)
    assert tree.depth() == 3
    assert tree.balance() == -1


def test_left_rotation_four_node_tree():
    """Test four nodes rotate left, no root change."""
    from bst import BST
    tree = BST([1, 2, 3, 4, 5])
    assert tuple(tree.in_order()) == (1, 2, 3, 4, 5)
    assert tuple(tree.breadth_first()) == (2, 1, 4, 3, 5)
    assert tuple(tree.pre_order()) == (2, 1, 4, 3, 5)
    assert tuple(tree.post_order()) == (1, 3, 5, 4, 2)
    assert tree.depth() == 3
    assert tree.balance() == 1


def test_right_left__rotation_five_node_tree():
    """Test three nodes rotate right, no root change."""
    from bst import BST
    tree = BST([1, 2, 5, 3, 4])
    assert tuple(tree.in_order()) == (1, 2, 3, 4, 5)
    assert tuple(tree.breadth_first()) == (2, 1, 4, 3, 5)
    assert tuple(tree.pre_order()) == (2, 1, 4, 3, 5)
    assert tuple(tree.post_order()) == (1, 3, 5, 4, 2)
    assert tree.depth() == 3
    assert tree.balance() == 1


def testt_left_right_rotation_five_node_tree():
    """Test three nodes rotate right, no root change."""
    from bst import BST
    tree = BST([4, 5, 1, 3, 2])
    assert tuple(tree.in_order()) == (1, 2, 3, 4, 5)
    assert tuple(tree.breadth_first()) == (4, 2, 5, 1, 3)
    assert tuple(tree.pre_order()) == (4, 2, 1, 3, 5)
    assert tuple(tree.post_order()) == (1, 3, 2, 5, 4)
    assert tree.depth() == 3
    assert tree.balance() == -1


def test_random_100_in_order_again(bst_100_rand):
    """Test random one retains order."""
    assert tuple(bst_100_rand.in_order()) == tuple(x for x in range(100))
