#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using dynamic programming to solve maximal square
 '''


# In this solution, I solve the dp problem from the right bottom of the martix,
# dp[i][j] represents the side length of maximum square which using (i,j) as the top left corner.


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

        def checkSquare(i,j,l):
            tmp = l
            for row in range(i, i+l+1):
                if matrix[row][j] == '0':
                    tmp = row - i - 1
            for col in range(j, j+l+1):
                if matrix[i][col] == '0':
                    tmp = min(tmp, col-j - 1)
            return tmp

        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[0])-1, -1, -1):
                if matrix[i][j] != '0':
                    dp[i][j] = 1
                    sub_len = dp[i+1][j+1]
                    if sub_len > 0:
                        tmp = checkSquare(i, j, sub_len)
                        dp[i][j] += tmp
                max_len = max(max_len, dp[i][j])

        return max_len**2
