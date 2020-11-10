#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using dfs to find maximum length of a concatenated string with unique characters.
 '''
class Solution(object):
    def __init__(self):
        self.maxlen = 0

    def dfs(self, arr, string, index):

        if len(string) != len(set(string)):
            return

        self.maxlen = max(self.maxlen, len(string))

        for i in range(index, len(arr)):
            self.dfs(arr, string+arr[i], i+1)

    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """

        self.dfs(arr, "", 0)

        return self.maxlen
