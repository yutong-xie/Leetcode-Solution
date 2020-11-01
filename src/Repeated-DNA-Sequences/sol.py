#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using set to find repeated DNA Sequences.
 '''

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []

        ans = set()

        h = set()

        for i in range(len(s)-9):
            if s[i:i+10] in h:
                ans.add(s[i:i+10])
            else:
                h.add(s[i:i+10])

        return list(ans)
