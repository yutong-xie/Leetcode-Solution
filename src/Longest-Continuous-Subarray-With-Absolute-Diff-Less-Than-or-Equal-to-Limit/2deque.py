#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using two deque to find longest continuous subarray with absolute diff less than limit.
 '''

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """

        import collections
        # using high, low to record the index of max/min number
        low, high = collections.deque([0]), collections.deque([0])
        ans = 1
        l = 0
        for i in range(1, len(nums)):
            while high and nums[high[-1]] < nums[i]:
                high.pop()
            high.append(i)

            while low and nums[low[-1]] > nums[i]:
                low.pop()
            low.append(i)

            while low and high and nums[high[0]] - nums[low[0]] > limit:
                left += 1
                if high[0] < left:
                    high.popleft()
                if low[0] < left:
                    low.popleft()

            ans = max(ans, i - l + 1)

        return ans
