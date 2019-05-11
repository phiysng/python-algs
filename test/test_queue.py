# -*- coding: utf-8 -*-

from src.Queue import Queue


def test_empty_queue():
    queue = Queue()
    assert len(queue) == 0
    assert queue.size() == 0

def test_nonempty_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    assert len(queue) == 3
    assert queue.dequeue() == 1

    assert queue.front() == 2

    assert len(queue) == 2
    assert queue.dequeue() == 2

    assert len(queue) == 1
    assert queue.dequeue() == 3

    assert len(queue) == 0
