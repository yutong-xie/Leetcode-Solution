#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using bidirectional dp to solve stock buying-selling problem
 '''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        dp_left = [0]*len(prices)
        dp_right = [0]*(len(prices)+1)
        
        low = prices[0]
        high = prices[-1]


        for i in range(1, len(prices)):
            low = min(low, prices[i])
            dp_left[i] = max(prices[i]-low, dp_left[i-1])

            r = len(prices) - 1 - i

            high = max(high, prices[r])
            dp_right[r] = max(high-prices[r], dp_right[r+1])

        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, dp_left[i]+dp_right[i+1])

        return max_profit
