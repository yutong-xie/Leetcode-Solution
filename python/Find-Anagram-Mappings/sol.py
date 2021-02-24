#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using hashmap to find anagram mappings.
 '''

class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        h = {}
        ans = []
        for i in range(len(B)):
            h[B[i]] = i

        for i in range(len(A)):
            ans.append(h[A[i]])

        return ans
