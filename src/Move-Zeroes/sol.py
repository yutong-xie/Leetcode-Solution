#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2021, Yutong Xie, UIUC.
    Using two pointers to move all zeroes to the end of an array.
 '''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nonzero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[nonzero] = nums[nonzero], nums[i]
                nonzero += 1
