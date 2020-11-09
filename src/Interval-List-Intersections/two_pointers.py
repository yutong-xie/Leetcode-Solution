#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using Two Pointers to find the interval intersection.
 '''


class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not B:
            return []

        a, b = 0, 0
        ans = []

        while a < len(A) and b < len(B):
            low = max(A[a][0], B[b][0])
            high = min(A[a][1], B[b][1])

            if low <= high:
                ans.append([low, high])

            if A[a][1] < B[b][1]:
                a += 1
            else:
                b += 1

        return ans
