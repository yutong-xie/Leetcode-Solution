#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2021, Yutong Xie, UIUC.
    Find the length of last word.
 '''

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        return len(s.split()[-1]) if len(s.split())!= 0 else 0
