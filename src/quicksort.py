# -*- coding: utf-8 -*-


'''
快排算法的简单实现
TODO:使用了O(n)的空间 两次遍历了数组
'''


def quicksort(arr: list) -> list:
    if len(arr) == 1 or len(arr) == 0:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    # 递归排序
    lr = quicksort(left)
    lr.append(pivot)
    rr = quicksort(right)
    return lr + rr
