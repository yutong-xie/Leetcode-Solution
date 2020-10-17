#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using Binary Search to find first and last position of an element 
 '''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if not nums:
            return [-1, -1]

        l = 0
        r = len(nums) - 1
        index = -1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if index == -1:
            return [-1, -1]

        l, r = index, index

        while l >= 0 and nums[l] == target:
            l -= 1
        while r < len(nums) and nums[r] == target:
            r += 1

        return [l+1, r-1]
