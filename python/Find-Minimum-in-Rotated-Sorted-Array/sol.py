#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using binary search to find minimum in rotated sorted array.
 '''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1

        if nums[l] <= nums[r]:
            return nums[0]

        while l <= r:
            mid = (l+r)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]

            if nums[mid] < nums[l]:
                r = mid - 1
            else:
                l = mid + 1
