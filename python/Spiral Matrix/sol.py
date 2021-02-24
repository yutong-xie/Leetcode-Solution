#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Create a new matrix to mark the visited element
 '''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        if not matrix:
            return ans

        R, C = len(matrix), len(matrix[0])
        visited = [[False]*C for _ in range(R)]

        dirc = [[0,1],[1,0],[0,-1],[-1,0]]


        r, c, count = 0, 0, 0
        for _ in range(R*C):
            ans.append(matrix[r][c])
            visited[r][c] = True
            newr, newc = r+dirc[count][0], c+dirc[count][1]
            if 0 <= newr < R and 0 <= newc < C and not visited[newr][newc]:
                r, c = newr, newc

            else:
                count = (count + 1) % 4
                r, c = r+dirc[count][0], c+dirc[count][1]

        return ans
