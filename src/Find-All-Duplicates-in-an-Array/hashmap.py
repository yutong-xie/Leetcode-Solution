#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using hashmap to find all duplicates in an array. 
 '''

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        h = set()
        ans = []
        for i in nums:
            if i in h:
                ans.append(i)
            else:
                h.add(i)

        return ans
