#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using hashmap to find the first missing positive number in an array.
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

        d = {}

        for i in range(l):
            d[nums[i]] = 1


        for i in range(1, l+1):
            if i not in d:
                return i

        return l+1
