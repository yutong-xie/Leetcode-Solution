#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using dp to solve stock buying-selling problem 
 '''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) < 2:
            return 0

        profit = 0
        low = prices[0]

        for i in range(len(prices)):
            low = min(low, prices[i])
            profit = max(profit, prices[i]-low)

        return profit
