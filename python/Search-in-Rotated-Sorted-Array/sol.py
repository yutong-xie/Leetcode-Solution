#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using random index to shuffle an array
 '''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l, r = 0, len(nums)-1
        while l <= r:

            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            # non rotated array
            if nums[mid] >= nums[l]:
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            # nums[mid] < nums[l]:   rotated array
            else:
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
