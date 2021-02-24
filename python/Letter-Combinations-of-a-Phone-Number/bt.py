#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using backtracking to find all letter combinations of phone number
 '''

 class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return ""

        hashmap = { "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6":  "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"
                    }

        ans = []
        def helper(index, s):
            if index >= len(digits):
                ans.append(s)
                return


            d = hashmap[digits[index]]
            for i in range(len(d)):
                helper(index+1, s+d[i])



        helper(0, "")

        return ans
