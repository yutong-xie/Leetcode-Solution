#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using dynamic programming to solve maximal square
 '''


# In this solution, I solve the dp problem from the top left of the martix,
# dp[i][j] represents the side length of maximum square which using (i,j) as the bottom right corner.


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        if not matrix[0]:
            return 0

        dp = [[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]

        max_len = 0

        for r in range(1, len(matrix)+1):
            for c in range(1, len(matrix[0])+1):

                if matrix[r-1][c-1] == '1':
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                    max_len = max(max_len, dp[r][c])

        return max_len**2
