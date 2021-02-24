#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using dynamic programming to solve longest string decode problem
 '''


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        dp = [0] * (len(s) + 1)

        dp[0] = 1

        # 0 cannot be decoded.
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(s)+1):

            if s[i-1] != '0':
                dp[i] += dp[i-1]

            if int(s[i-2 : i]) <= 26 and int(s[i-2 : i]) >= 10:
                dp[i] += dp[i-2]


        return dp[-1]
