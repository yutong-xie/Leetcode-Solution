#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using expand around center algorithm to solve longest palindromic substring problem
 '''


 class Solution(object):
     def longestPalindrome(self, s):
         """
         :type s: str
         :rtype: str
         """
         start = 0
         length = 0


         def getlen(l, r):
             while l >= 0 and r < len(s) and s[l] == s[r]:
                 l -= 1
                 r += 1
             # l and r right now are not the begining and ending index of longest palindrome,
             # they represent for begining - 1 and ending + 1
             return r - l - 1


         for i in range(len(s)):
             tmp = max(getlen(i,i), getlen(i,i+1))
             if tmp > length:
                 length = tmp
                 start = i - (tmp - 1) // 2

         return s[start: start+length]
