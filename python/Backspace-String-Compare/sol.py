#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using stack to conduct backspace string compare.
 '''

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s = []
        t = []
        for i in S:
            if i != "#":
                s.append(i)
            else:
                if s:
                    s.pop()
        for i in T:
            if i != "#":
                t.append(i)
            else:
                if t:
                    t.pop()

        return "".join(s) == "".join(t)
