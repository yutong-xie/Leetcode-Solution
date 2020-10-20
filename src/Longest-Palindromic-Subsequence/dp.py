#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using Dynamic Programming to find longest Palindromic Subsequence.
 '''

 class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [[1]*len(s) for _ in range(len(s))]

        for l in range(1, len(s)):
            for start in range(len(s)-l):
                end = start + l

                tmp = 0

                if s[start] == s[end]:
                    tmp += 2
                    if end - start > 1:
                        tmp += dp[start+1][end-1]
                else:
                    tmp = max(dp[start+1][end], dp[start][end-1])

                dp[start][end] = tmp

        return dp[0][-1]
