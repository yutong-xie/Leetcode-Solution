
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using dynamic programming to solve maximum product subarray problem
 '''

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            tmp_max = max(curr, max_so_far*curr, min_so_far*curr)
            min_so_far = min(curr, max_so_far*curr, min_so_far*curr)
            max_so_far = tmp_max

            result = max(result, max_so_far)

        return result
