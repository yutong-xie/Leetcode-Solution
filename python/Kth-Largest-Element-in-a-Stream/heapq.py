#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using heapq to find kth largest element in a stream
 '''

 import heapq as hq
 class KthLargest(object):

     def __init__(self, k, nums):
         """
         :type k: int
         :type nums: List[int]
         """
         self.heap = []
         self.k = k
         for i in range(len(nums)):
             if i < k:
                 hq.heappush(self.heap, nums[i])
             else:
                 hq.heappushpop(self.heap, nums[i])


     def add(self, val):
         """
         :type val: int
         :rtype: int
         """

         if len(self.heap) < self.k:
             hq.heappush(self.heap, val)
         else:
             hq.heappushpop(self.heap, val)

         return self.heap[0]


 # Your KthLargest object will be instantiated and called as such:
 # obj = KthLargest(k, nums)
 # param_1 = obj.add(val)
