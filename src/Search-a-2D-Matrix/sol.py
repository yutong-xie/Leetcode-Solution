#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Tricky method to search elements in 2D matrix.
 '''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        index = -1

        for i in range(len(matrix)-1):
            if matrix[i][0] <= target < matrix[i+1][0]:
                index = i
                break

        if index == -1:
            index = len(matrix)-1

        for i in range(len(matrix[0])):
            if matrix[index][i] == target:
                return True

        return False
