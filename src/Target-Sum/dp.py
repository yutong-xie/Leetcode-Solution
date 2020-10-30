#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using Dynamic Programming to find out how many ways to assign symbols to make sum of integers equal to target S.
 '''

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        import collections

        if len(nums) == 1:
            return 1 if abs(nums[0]) == abs(S) else 0

        d = collections.defaultdict(int)
        d[nums[0]] += 1
        d[-nums[0]] += 1

        for i in range(1, len(nums)):
            new_d = collections.defaultdict(int)
            for j in d:
                plus_num = j + nums[i]
                new_d[plus_num] += d[j]
                minus_num = j - nums[i]
                new_d[minus_num] += d[j]

            d = new_d

        return d[S]
