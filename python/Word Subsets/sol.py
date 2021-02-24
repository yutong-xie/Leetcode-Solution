#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using hashmap to find word subsets.
 '''

class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        import collections

        hashmap = collections.defaultdict(int)

        for word in B:
            wordcount = collections.Counter(word)
            for i in wordcount:
                hashmap[i] = max(hashmap[i], wordcount[i])

        ans = []

        def isSubset(word):
            wordcount = collections.Counter(word)
            for i in hashmap:
                if wordcount[i] < hashmap[i]:
                    return False
            return True

        for word in A:
            if isSubset(word):
                ans.append(word)

        return ans
