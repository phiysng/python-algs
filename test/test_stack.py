# -*- coding: utf-8 -*-

from src.Stack import Stack


def test_empty_stack():
    s = Stack()
    assert s.size() == 0
    assert len(s) == 0


def test_nonempty_stack():
    s = Stack()
    s.push(1)
    s.push(2)

    assert len(s) == 2
    assert s.pop() == 2

    assert len(s) == 1
    assert s.pop() == 1

    assert len(s) == 0
    assert s.pop() == None
