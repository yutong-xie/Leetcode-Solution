#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using dp to find minimum path sum for a triangle.
 '''

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        l = len(triangle)

        dp = [[0 for _ in range(l)] for _ in range(l)]

        dp[0][0] = triangle[0][0]

        if l == 1:
            return dp[0][0]

        dp[1][0] = dp[0][0] + triangle[1][0]
        dp[1][1] = dp[0][0] + triangle[1][1]

        for i in range(2, l):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j]+ triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1]+ triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

        return min(dp[-1])
