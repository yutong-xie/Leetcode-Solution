#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using dynamic programming to solve trapping rain water problem
 '''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left_max = [0]*len(height)
        right_max = [0]*len(height)
        ans = 0

        # Initialize two dp arrays
        left_max[0] = height[0]
        right_max[len(height)-1] = height[-1]

        for i in range(1, len(height)):
            left_max[i] = max(height[i], left_max[i-1])

        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])

        for i in range(len(height)):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans
