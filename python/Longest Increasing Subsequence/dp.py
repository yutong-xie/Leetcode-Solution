#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using DP to solve longest increasing subsequence problem.
 '''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        dp = [0]*len(nums)
        dp[0] = 1
        ans = 1

        for i in range(1,len(nums)):
            max_cur = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    max_cur = max(max_cur, dp[j])

            dp[i] = max_cur + 1
            ans = max(ans, dp[i])

        return ans
