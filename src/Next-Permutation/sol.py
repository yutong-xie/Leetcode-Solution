#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Find the next permutation of an array. 
 '''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = len(nums) - 2
        while index >= 0 and nums[index+1] <= nums[index]:
            index -= 1

        if index >= 0 :
            right = len(nums) - 1
            while right > index and nums[right] <= nums[index]:
                right -= 1

            nums[index],  nums[right] = nums[right], nums[index]

        i = index + 1
        j = len(nums) - 1

        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
