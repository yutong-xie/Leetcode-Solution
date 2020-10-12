#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using doubly linked node to implement LRU Cache.
 '''

class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache(object):

    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)

    def pop_tail(self):
        res = self.tail.prev
        self.remove_node(res)
        return res


    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.capacity = capacity
        self.size = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            node = self.d[key]
            self.move_to_head(node)
            return node.val

        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if key in self.d:
            node = self.d[key]
            node.val = value
            self.move_to_head(node)
        else:
            new_node = DLinkedNode()
            new_node.key = key
            new_node.val = value

            self.d[key] = new_node
            self.add_node(new_node)
            self.size += 1

            if self.size > self.capacity:
                tail = self.pop_tail()
                del self.d[tail.key]
                self.size -= 1




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
