#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using backtracking to solve permutation problem
 '''

 class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtracking(nums, current):
            if nums == []:
                result.append(current)
                return

            for i in range(len(nums)):
                backtracking(nums[:i]+nums[i+1:], current+[nums[i]])

        backtracking(nums, [])

        return result
        
