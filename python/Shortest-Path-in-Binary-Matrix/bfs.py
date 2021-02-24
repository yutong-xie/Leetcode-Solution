#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using BFS to solve the problem.
 '''

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] or grid[-1][-1]:
            return -1

        R, C = len(grid), len(grid[0])

        visited = {(0,0)}

        bfs = collections.deque([(0, 0, 1)])

        while bfs:
            i, j, cost = bfs.popleft()

            if i == R-1 and j == C-1:
                return cost

            for ix, iy in [(1, 0), (-1, 0), (0, -1), (0, 1), (-1, 1), (1, -1), (1, 1), (-1, -1)]:
                ni, nj, ncost = i+ix, j+iy, cost+1
                if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] == 0 and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    bfs.append((ni, nj, ncost))

        return -1
