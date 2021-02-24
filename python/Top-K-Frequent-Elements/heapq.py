#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using heap to find top k frequent elements
 '''


 class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        import heapq
        from collections import Counter

        d = Counter(nums)

        q = [(-v, key) for key, v in d.items()]

        heapq.heapify(q)

        return [heapq.heappop(q)[1] for _ in range(k)]
