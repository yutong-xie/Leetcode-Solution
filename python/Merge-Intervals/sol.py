#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2021, Yutong Xie, UIUC.
    Merge several intervals by sorting them.
 '''


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)
        start, end = intervals[0]
        ans = []

        for i in range(1, len(intervals)):
            l, r = intervals[i]
            if l > end:
                ans.append([start, end])
                start, end = l, r
            else:
                end = max(end, r)

        ans.append([start, end])

        return ans
