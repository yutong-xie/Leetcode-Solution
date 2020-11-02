#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using hashmap to check valid anagram string
 '''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        import collections

        h = collections.defaultdict(int)

        for i in s:
            h[i] += 1

        for i in t:
            h[i] -= 1

        for i in h:
            if h[i] != 0:
                return False

        return True
