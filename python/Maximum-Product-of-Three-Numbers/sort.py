#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Copyright 2021, Yutong Xie, UIUC.
    Using for sort to find maximum product of three numbers
'''

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums = sorted(nums)
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])