#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using greedy algorithm to find maximum subarray
 '''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_sum = -float('inf')
        max_current = -float('inf')

        for i in range(len(nums)):
            max_current = max(max_current+nums[i], nums[i])
            max_sum = max(max_sum, max_current)

        return max_sum
