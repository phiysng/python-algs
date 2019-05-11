# -*- coding: utf-8 -*-

from random import shuffle
from src.quicksort import quicksort


def test_quicksort():
    
    arr = list(range(20))
    shuffle(arr)
    assert quicksort(arr) == list(range(20))

    arr = [0]
    assert quicksort(arr) == [0]

    arr = [0, 0]
    assert quicksort(arr) == [0, 0]

    arr = [0, 1]
    assert quicksort(arr) == [0, 1]
