#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using ordered dictionary to find longest substring with no more than k distinct characters.

    Time Complexity: O(N)
    All operations with ordered dictionary : insert/get/delete/popitem (put/containsKey/remove) are done in a constant time.
 '''

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        import collections
        if not s or k == 0:
            return 0

        d = collections.OrderedDict()

        l, r = 0, 0

        ans = 0

        while r < len(s):
            if s[r] in d:
                del d[s[r]]

            d[s[r]] = r
            r += 1
            if len(d) == k + 1:
                _, index = d.popitem(False)
                l = index + 1

            ans = max(ans, r-l)

        return ans
