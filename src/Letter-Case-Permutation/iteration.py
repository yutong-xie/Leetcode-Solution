#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2021, Yutong Xie, UIUC.
    Find letter case permutation using iteration.
 '''


 class Solution(object):
     def letterCasePermutation(self, S):
         """
         :type S: str
         :rtype: List[str]
         """
         ans = [[]]

         for char in S:
             n = len(ans)
             if char.isalpha():
                 for i in range(n):
                     ans.append(ans[i][:])
                     ans[i].append(char.upper())
                     ans[n+i].append(char.lower())
             else:
                 for i in range(n):
                     ans[i].append(char)

         return map("".join, ans)
