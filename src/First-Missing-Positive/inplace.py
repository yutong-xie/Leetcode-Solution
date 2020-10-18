#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using in-place method to find first missing positive integer
 '''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 1 not in nums:
            return 1

        l = len(nums)

        if l == 1:
            return 2

        for i in range(l):
            if nums[i] <= 0 or nums[i] > l:
                nums[i] = 1

        for i in range(l):
            tmp = abs(nums[i])
            if tmp == l:
                nums[0] = -abs(nums[0])
            else:
                nums[tmp] = -abs(nums[tmp])

        for i in range(1,l):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return l

        return l+1
