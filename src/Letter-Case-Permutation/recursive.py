#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2021, Yutong Xie, UIUC.
    Find letter case permutation using recursion.
 '''


 class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = []
        d = {}
        for i in "abcdefghijklmnopqrstuvwxyz":
            d[i] = [i, i.upper()]

        def helper(s, i):
            if len(s) == len(S):
                ans.append(s)
                return
            if S[i].isdigit():
                helper(s+S[i], i+1)
            else:
                tmp = S[i].lower()
                for a in d[tmp]:
                    helper(s+a, i+1)

        helper("", 0)

        return ans
