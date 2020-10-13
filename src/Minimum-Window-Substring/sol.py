#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using sliding window to find the minimum window substring 
 '''


class Solution(object):
    import collections
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        l, r = 0, 0

        ans = float("inf"), None, None

        d_t = collections.Counter(t)
        goal = len(d_t)

        # select the elements appear in t from s
        new_s = []
        for i in range(len(s)):
            if s[i] in d_t:
                new_s.append((s[i], i))


        l, r = 0, 0

        d_s = {}
        current = 0

        while r < len(new_s):
            char = new_s[r][0]
            d_s[char] = d_s.get(char, 0) + 1
            if d_s[char] == d_t[char]:
                current += 1

            while l <= r and current == goal:
                char = new_s[l][0]
                start = new_s[l][1]
                end = new_s[r][1]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                d_s[char] -= 1
                if d_s[char] < d_t[char]:
                    current -= 1
                l += 1

            r += 1



        return "" if ans[0] == float("inf") else s[ans[1] : ans[2]+1]
