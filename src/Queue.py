# -*- coding: utf-8 -*-

class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    def front(self):
        if len(self.queue)==0:
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def __len__(self):
        return self.size()