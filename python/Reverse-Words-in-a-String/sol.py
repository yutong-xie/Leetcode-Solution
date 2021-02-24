#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Reverse words in the string 
 '''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        return " ".join(s.split()[::-1])
