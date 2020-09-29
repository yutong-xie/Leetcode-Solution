#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using brute force to find longest common prefix
 '''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        ans = strs[0]

        for i in range(len(strs)):
            while strs[i].find(ans) != 0:
                ans = ans[:-1]
                if ans == "":
                    return ans
        return ans
