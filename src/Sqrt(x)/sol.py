#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using binary search to find sqrt x 
 '''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        l, r = 2, x//2

        while l <= r:
            mid = (l+r) // 2
            s = mid*mid

            if s == x:
                return mid
            elif s < x:
                l = mid + 1
            else:
                r = mid - 1

        return r
