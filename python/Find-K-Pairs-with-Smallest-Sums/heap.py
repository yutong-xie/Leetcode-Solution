#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using heap to solve the problem
 '''

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """

        import heapq as hq

        heap = []

        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                s = nums1[i] + nums2[j]
                if len(heap) < k:
                    hq.heappush(heap, (-s, i, j))

                else:
                    if -s > heap[0][0]:
                        hq.heappop(heap)
                        hq.heappush(heap, (-s, i, j))
                    else:
                        break



        ans = []
        for _, i, j in heap:
            ans.append([nums1[i], nums2[j]])

        return ans
