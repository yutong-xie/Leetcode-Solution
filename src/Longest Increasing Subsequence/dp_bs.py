#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using DP + Binary Search to solve longest increasing subsequence problem.
 '''

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def binarysearch(dp, l, length, num):
            if num < dp[l]:
                return -1
            if num > dp[length-1]:
                return length
            r = length - 1
            while l <= r:
                mid = (l + r) // 2
                if num < dp[mid]:
                    if num > dp[mid-1]:
                        return mid
                    else:
                        r = mid - 1
                elif num > dp[mid]:
                    if num < dp[mid+1]:
                        return mid + 1
                    else:
                        l = mid + 1
                else:
                    return mid

        dp = [0]*len(nums)
        l = 0

        for num in nums:
            i = binarysearch(dp, 0, l, num)
            if i < 0:
                i = 0
            dp[i] = num
            if i == l:
                l += 1

        return l
