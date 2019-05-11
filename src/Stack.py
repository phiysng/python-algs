# -*- coding: utf-8 -*-

'''
简单的Stack实现 Adapter of List.
'''


class Stack(object):
    """一个只允许 pop && push 操作的 Stack"""

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) < 1:
            return None

        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

    def __len__(self):
        return self.size()
