# coding:utf8
"""
    146. LRU 缓存机制
"""

class LRUCache:

    def __init__(self, capacity: int):
        pass


    def get(self, key: int) -> int:
        pass


    def put(self, key: int, value: int) -> None:
        pass



class Node:

    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None

class DoubleLinkedList:

    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0


    



