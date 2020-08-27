#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using dynamic programming to solve maximum product subarray problem
 '''

## This method is correct but may exceed the time limitation.


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product = - sys.maxint - 1

        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]

        for i in range(len(nums) -1, -1, -1):
            for j in range(i, len(nums)):
                if i == j:
                    dp[i][j] = nums[i]
                elif i == j - 1:
                    dp[i][j] = nums[i]*nums[j]
                else:
                    dp[i][j] = dp[i+1][j-1]*nums[i]*nums[j]

                max_product = max(max_product, dp[i][j])

        return max_product
