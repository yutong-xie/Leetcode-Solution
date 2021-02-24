#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using BFS to solve the problem.
 '''

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        R, C = len(grid), len(grid[0])

        ans = 0

        bfs = []

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    bfs.append((r,c))

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while bfs:
            new_bfs = []
            for r,c in bfs:
                for ir, ic in direction:
                    new_r, new_c = r + ir, c + ic
                    if 0 <= new_r < R and 0 <= new_c < C and grid[new_r][new_c] == 1:
                        new_bfs.append((new_r, new_c))
                        grid[new_r][new_c] = 2
            bfs = new_bfs

            if bfs != []:
                ans += 1

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    return -1

        return ans
