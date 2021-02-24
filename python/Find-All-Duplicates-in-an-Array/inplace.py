#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using one pass to find all duplicates in an array. 
 '''

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        for i in range(len(nums)):
            index = abs(nums[i]) -1
            if nums[index] < 0:
                ans.append(abs(nums[i]))
            else:
                nums[index] *= -1

        return ans
