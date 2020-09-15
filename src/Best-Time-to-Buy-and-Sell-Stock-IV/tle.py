#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    One pass method to solve stock buying-selling problem
 '''


# Correct algorithm but TLE
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2 or k == 0:
            return 0

        dp = [float("-inf")]*2*k
        dp[0] = -prices[0]
        for p in prices:
            for i in range(k):
                if i == 0:
                    dp[0] = max(dp[0], -p)
                else:
                    dp[2*i] = max(dp[2*i], dp[2*i-1]-p)
                dp[2*i+1] = max(dp[2*i+1], dp[2*i]+p)

        return dp[-1]
