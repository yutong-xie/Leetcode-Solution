#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using dynamic programming and backtracking to solve word break problem 
 '''


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        ans = []
        if not dp[-1]:
            return ans

        def helper(tmp, l):
            if l >= len(s):
                tmp = " ".join(tmp)
                ans.append(tmp)

            for i in range(l+1, len(s)+1):
                if dp[i]:
                    word = s[l:i]
                    if word in wordDict:
                        helper(tmp+[word], i)


        helper([], 0)

        return ans
