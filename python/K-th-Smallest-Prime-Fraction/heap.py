#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using heap to find kth smallest prime fraction 
 '''

class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        if not A:
            return []
        A = sorted(A)

        heap = []

        import heapq as hq
        count = 0
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                num = A[i]/float(A[j])
                tmp  = (-num, i, j)
                if count < K:
                    hq.heappush(heap, tmp)
                    count += 1
                else:
                    hq.heappushpop(heap, tmp)

        frac, i, j = hq.heappop(heap)

        return [A[i], A[j]]
