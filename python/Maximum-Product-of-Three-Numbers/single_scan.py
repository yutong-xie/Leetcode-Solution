#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Copyright 2021, Yutong Xie, UIUC.
    Using for loop to find maximum product of three numbers
'''

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min1, min2 = float("inf"), float("inf")
        
        max1, max2, max3 = -float("inf"), -float("inf"), -float("inf")
        
        for i in range(len(nums)):
            n = nums[i]
            if n <= min1:
                min1, min2 = n, min1
            elif n <= min2:
                min2 = n 
            if n >= max3:
                max1, max2, max3 = max2, max3, n
            elif n >= max2:
                max1, max2 = max2, n
            elif n >= max1:
                max1 = n
                
        return max(min1*min2*max3, max1*max2*max3)    
        