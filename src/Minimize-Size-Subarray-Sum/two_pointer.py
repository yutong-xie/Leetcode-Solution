#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using two pointers to find the minimum size subarray sum. 
 '''

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or sum(nums) < s:
            return 0

        l = 0
        ans = float("inf")
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            while sums >= s:
                ans = min(ans, i-l+1)
                sums -= nums[l]
                l += 1

        return ans
