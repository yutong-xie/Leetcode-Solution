#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    One pass method to solve stock buying-selling problem
 '''

 class Solution(object):
     def maxProfit(self, prices):
         """
         :type prices: List[int]
         :rtype: int
         """
         if len(prices) < 2:
             return 0

         b1,b2 = float('inf'), float('inf')
         s1,s2 = 0, 0

         for p in prices:
             b1 = min(b1,p)
             s1 = max(s1, p-b1)
             b2 = min(b2, p-s1)
             s2 = max(s2, p-b2)

         return s2

# 把买入设置成负数，卖出设置成正数
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        b1,b2 = -prices[0], float('-inf')
        s1,s2 = float('-inf'), float('-inf')

        for p in prices:
            b1 = max(b1, -p)
            s1 = max(s1, b1+p)
            b2 = max(b2, s1-p)
            s2 = max(s2, b2+p)

        return s2
