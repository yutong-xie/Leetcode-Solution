#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using Greedy Algorithm to solve non-overlapping intervals problem
 '''


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        n = len(intervals)
        # sorted with end point
        intervals = sorted(intervals, key = lambda i: i[1])

        end = intervals[0][1]
        count = 1
        for i in range(1, n):
            start = intervals[i][0]
            if start >= end:
                count += 1
                end = intervals[i][1]

        return n-count
