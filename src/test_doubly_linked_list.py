"""Tests for doubly-linked list data structure."""
import pytest


def test_dll_push():
    # import
    # assert val of pushed node == val of dll.head
    # assert val of pushed node to empty list == dll.head and == dll.tail


def test_dll_push_none():
    # import
    # with pytest raise our exception:
    # run that shit


def test_dll_append():
    # import
    # assert val of pushed node == val of dll.tail
    # assert val of pushed node to empty list == dll.head and == dll.tail


def test_dll_append_none():
    # import
    # with pytest raise our exception:
    # run that shit


def test_dll_pop():
    # import
    # new_head = dll.head.next
    # assert dll.pop() == (old head)
    # assert dll.head = new_head


def test_dll_pop_empty():
    # import
    # with pytest raise our exception:
    # run that shit


def test_dll_shift():
    # import
    # new_tail = dll.tail.previous
    # assert dll.shift() == (old tail)
    # assert dll.tail = new_tail


def test_dll_shift_empty():
    # import
    # with pytest raise our exception:
    # run that shit


def test_dll_remove():
    #import
    # assert len(dll.remove(NODE)) == old len -1
    # assert NODE.prev.next = NODE.next
    # assert NODE.next.prev = NODE.prev


def test_dll_remove_invalid():
    # import
    # with pytest raise our exception:
    # run that shit


def test_dll_len():
    # import
    # assert len(pushed dll) == len
    # assert len(empty dll) == 0
