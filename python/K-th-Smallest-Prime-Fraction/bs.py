#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using binary search to find the kth smallest prime fraction.
 '''

class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        n = len(A)
        def under(x):
            count = 0
            i = -1
            best = 0, 0, 0
            for j in range(1, n):
                while A[i+1] < A[j]*x:
                    i += 1
                count += i+1
                if i >= 0 :
                    m, i1, i2 = best
                    if A[i]/float(A[j]) > m:
                        best = A[i]/float(A[j]), A[i], A[j]

            return count, best

        l, h = 0.0, 1.0

        while h - l > 1e-9:
            mid = (h+l)/2.0
            count, best = under(mid)
            if count < K:
                l = mid
            else:
                ans = best
                h = mid


        return [ans[1], ans[2]]
