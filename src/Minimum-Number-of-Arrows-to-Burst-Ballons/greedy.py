#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using Greedy Algorithm to solve balloon burst problem.
 '''

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points = sorted(points, key=lambda i:i[1])

        count = 1
        end = points[0][1]
        for i in points:
            start = i[0]
            if start > end:
                count += 1
                end = i[1]

        return count
