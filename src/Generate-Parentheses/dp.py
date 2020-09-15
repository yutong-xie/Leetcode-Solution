#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using backtracking to generate parentheses
 '''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if n == 0:
            return []


        ans = []

        def backtracking(l,r,s):
            if l == 0 and r == 0:
                ans.append(s)
                return

            if l > 0:
                backtracking(l-1, r, s+'(')

            if l < r:
                backtracking(l, r-1, s+')')



        backtracking(n,n,"")

        return ans
