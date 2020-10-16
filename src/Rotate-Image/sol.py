#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Rotate the image in array format
 '''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix[0])

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()
