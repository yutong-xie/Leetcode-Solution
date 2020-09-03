#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using dynamic programming to solve House Robber problem.
 '''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp = [0]*(len(nums)+1)

        dp[1] = nums[0]

        for i in range(1, len(nums)):
            dp[i+1] = max(dp[i-1]+nums[i], dp[i])

        return dp[-1]
