#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using dynamic programming to solve longest palindromic substring problem
 '''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = [[False for i in range(len(s))] for j in range(len(s))]

        max_len = 0
        start = 0


        # The reason for choosing reverse order is that we need to make sure the dp solve the problem from bottom to top,
        # which means that when we solve dp[i][j], we must know the value of dp[i+1][j-1]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):

                if j == i or j - i == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]

                if dp[i][j] and j-i+1 > max_len:
                    max_len = j-i+1
                    start = i


        return s[start: start+max_len]
