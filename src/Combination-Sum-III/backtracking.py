#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using back tracking to calculate the combination sunm
 '''

 class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if k >= n:
            return []
        
        com = []

        def backtrack(nums, n, k, start):
            if n == 0 and k == 0:
                com.append(nums)
                return
            if n <= 0 or k == 0 or start > 9:
                return


            for i in range(start,10):
                backtrack(nums+[i], n-i, k-1, i+1)

        backtrack([], n, k ,1)

        return com
