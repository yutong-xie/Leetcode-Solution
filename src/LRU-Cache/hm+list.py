#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using hashmap and list to implement LRU Cache.
 '''


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = {}
        self.r = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            self.r.remove(key)
            self.r.append(key)
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
            self.d[key] = value
            self.r.remove(key)
            self.r.append(key)
        else:
            if len(self.r) < self.capacity:
                self.d[key] = value
                self.r.append(key)
            else:
                cur = self.r[0]
                self.r.remove(cur)
                del self.d[cur]
                self.d[key] = value
                self.r.append(key)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
