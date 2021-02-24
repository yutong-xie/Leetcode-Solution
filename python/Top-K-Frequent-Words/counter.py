#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using Counter to get top k frequent words
 '''


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        import collections
        d = collections.Counter(words)
        d = sorted(d.keys(), key = lambda s: (-d[s], s))


        return d[:k]
