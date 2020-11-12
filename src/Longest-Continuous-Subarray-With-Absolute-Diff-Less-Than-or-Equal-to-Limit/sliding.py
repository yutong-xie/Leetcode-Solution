
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using sliding window to find longest continuous subarray with absolute diff less than limit.
 '''

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """

        l, r = 0, 0
        low, high = nums[0], nums[0]
        ans = 0
        while r < len(nums):
            low = min(nums[r], low)
            high = max(nums[r], high)
            if abs(high - low) <= limit:
                ans = max(ans, r-l+1)
            else:
                if low == nums[l]:
                    low = min(nums[l+1: r+1])
                if high == nums[l]:
                    high = max(nums[l+1: r+1])
                l +=1
            r += 1

        return ans
