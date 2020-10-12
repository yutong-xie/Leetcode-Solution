#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using ordered dictionary to implement LRU cache
 '''


class LRUCache(object):
    from collections import OrderedDict
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            self.d.move_to_end(key)
            return self.d[key]

        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.d:
            self.d.move_to_end(key)

        self.d[key] = value
        if len(self.d) > self.capacity:
            self.d.popitem(last=False)





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
