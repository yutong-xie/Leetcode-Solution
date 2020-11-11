#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using brute force to solve the problem.
 '''

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        ans = [nums[0]]

        for i in range(1, len(nums)):
            ans.append(ans[i-1]+nums[i])

        return ans
